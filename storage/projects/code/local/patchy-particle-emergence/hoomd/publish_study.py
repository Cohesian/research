"""Publish the executed notebook and selected study figures to Research storage."""

from __future__ import annotations

import base64
from pathlib import Path
from shutil import copy2

import nbformat


ROOT = Path(__file__).resolve().parent
RESEARCH = next(
    parent for parent in ROOT.parents if (parent / "contributor.toml").is_file()
)
TARGET = (
    RESEARCH
    / "storage"
    / "documents"
    / "local"
    / "T-physics"
    / "L-emergence"
    / "L-patchy-particle-emergence"
)

REPORT_FIGURES = (
    "condition-comparison.png",
    "energy-comparison.png",
    "peak-structures.png",
)


def refresh_report_figures(notebook: nbformat.NotebookNode, report: Path) -> None:
    """Replace saved notebook figures with the current report images."""

    for name in REPORT_FIGURES:
        source = report / name
        if not source.is_file():
            raise FileNotFoundError(f"Missing generated report figure: {source}")

        matching_cells = [
            cell
            for cell in notebook.cells
            if cell.cell_type == "code" and name in "".join(cell.source)
        ]
        if len(matching_cells) != 1:
            raise RuntimeError(
                f"Expected one notebook cell for {name}, found {len(matching_cells)}"
            )

        image_outputs = [
            output
            for output in matching_cells[0].outputs
            if output.output_type in {"display_data", "execute_result"}
            and "image/png" in output.get("data", {})
        ]
        if len(image_outputs) != 1:
            raise RuntimeError(
                f"Expected one saved PNG output for {name}, found {len(image_outputs)}"
            )

        image_outputs[0].data["image/png"] = base64.b64encode(
            source.read_bytes()
        ).decode("ascii")


def publish() -> None:
    notebook_source = ROOT / "notebooks" / "02-controlled-emergence-study.ipynb"
    notebook = nbformat.read(notebook_source, as_version=4)
    code_cells = [cell for cell in notebook.cells if cell.cell_type == "code"]
    if not code_cells or any(cell.execution_count is None for cell in code_cells):
        raise RuntimeError(
            "Notebook is not fully executed. Run `pixi run notebook-execute` first."
        )

    TARGET.mkdir(parents=True, exist_ok=True)
    assets = TARGET / "E-04-experimental-laboratory"
    assets.mkdir(parents=True, exist_ok=True)

    report = ROOT / "outputs" / "study" / "report"
    refresh_report_figures(notebook, report)
    nbformat.write(notebook, TARGET / "E-04-experimental-laboratory.ipynb")

    for name in REPORT_FIGURES:
        source = report / name
        copy2(source, assets / name)

    print(TARGET)


if __name__ == "__main__":
    publish()
