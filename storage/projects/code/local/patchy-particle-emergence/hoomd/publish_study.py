"""Publish the executed notebook and selected study figures to Research storage."""

from __future__ import annotations

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

    copy2(notebook_source, TARGET / "E-04-experimental-laboratory.ipynb")
    report = ROOT / "outputs" / "study" / "report"
    for name in (
        "condition-comparison.png",
        "energy-comparison.png",
        "peak-structures.png",
    ):
        source = report / name
        if not source.is_file():
            raise FileNotFoundError(f"Missing generated report figure: {source}")
        copy2(source, assets / name)

    print(TARGET)


if __name__ == "__main__":
    publish()
