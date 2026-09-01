"""Aggregate the controlled HOOMD study into comparison figures."""

from __future__ import annotations

import csv
import json
from pathlib import Path
import statistics
from typing import Any

import matplotlib.pyplot as plt
import numpy as np

from config import load_config
from render import draw_frame, frame_view


METRICS = (
    ("maximum_largest_component_fraction", "maximum component"),
    ("tail_largest_component_fraction", "tail component"),
    ("tail_mean_degree", "tail mean degree"),
    ("tail_orientational_order", "tail orientational order"),
)


def read_rows(path: Path) -> list[dict[str, str]]:
    with path.open(newline="", encoding="utf-8") as stream:
        return list(csv.DictReader(stream))


def condition_order(rows: list[dict[str, str]]) -> list[str]:
    return list(dict.fromkeys(row["condition"] for row in rows))


def representative_rows(rows: list[dict[str, str]]) -> dict[str, dict[str, str]]:
    representatives: dict[str, dict[str, str]] = {}
    for condition in condition_order(rows):
        candidates = [row for row in rows if row["condition"] == condition]
        values = [float(row["maximum_largest_component_fraction"]) for row in candidates]
        median = statistics.median(values)
        representatives[condition] = min(
            candidates,
            key=lambda row: abs(
                float(row["maximum_largest_component_fraction"]) - median
            ),
        )
    return representatives


def comparison_figure(rows: list[dict[str, str]], output: Path) -> None:
    conditions = condition_order(rows)
    figure, axes = plt.subplots(2, 2, figsize=(12, 8), constrained_layout=True)
    rng = np.random.default_rng(2026)
    for axis, (metric, title) in zip(axes.flat, METRICS, strict=True):
        for index, condition in enumerate(conditions):
            values = np.asarray(
                [
                    float(row[metric])
                    for row in rows
                    if row["condition"] == condition
                ]
            )
            jitter = rng.uniform(-0.06, 0.06, size=len(values))
            axis.scatter(
                np.full(len(values), index) + jitter,
                values,
                color="#674ea7",
                alpha=0.8,
                zorder=2,
            )
            axis.errorbar(
                index,
                np.mean(values),
                yerr=np.std(values, ddof=1) if len(values) > 1 else 0.0,
                fmt="o",
                color="#ef8354",
                capsize=4,
                linewidth=1.8,
                zorder=3,
            )
        axis.set(
            title=title,
            xticks=range(len(conditions)),
            xticklabels=[name.replace("--", "\n") for name in conditions],
        )
        axis.grid(axis="y", alpha=0.2)
    figure.suptitle("Controlled HOOMD study — seed observations and mean ± SD")
    figure.savefig(output, dpi=180)
    plt.close(figure)


def energy_figure(
    representatives: dict[str, dict[str, str]],
    output: Path,
) -> None:
    figure, axes = plt.subplots(2, 2, figsize=(12, 8), constrained_layout=True)
    for axis, (condition, row) in zip(
        axes.flat,
        representatives.items(),
        strict=True,
    ):
        observations = read_rows(Path(row["observables"]))
        time = [float(item["time"]) for item in observations]
        axis.plot(time, [float(item["potential_energy"]) for item in observations], label="U")
        axis.plot(time, [float(item["kinetic_energy"]) for item in observations], label="K")
        axis.set(
            title=f"{condition.replace('--', ' · ')} · seed {row['seed']}",
            xlabel="time",
            ylabel="reduced energy",
        )
        axis.legend()
        axis.grid(alpha=0.2)
    figure.suptitle("Representative energy trajectories")
    figure.savefig(output, dpi=180)
    plt.close(figure)


def peak_snapshot_figure(
    representatives: dict[str, dict[str, str]],
    output: Path,
) -> dict[str, dict[str, float | int]]:
    import gsd.hoomd

    figure, axes = plt.subplots(2, 2, figsize=(12, 11), constrained_layout=True)
    selected: dict[str, dict[str, float | int]] = {}
    for axis, (condition, row) in zip(
        axes.flat,
        representatives.items(),
        strict=True,
    ):
        config = load_config(row["config"])
        with gsd.hoomd.open(name=row["trajectory"], mode="r") as trajectory:
            views = [
                frame_view(frame, index, config)
                for index, frame in enumerate(trajectory)
            ]
        view = max(views, key=lambda item: item.largest_component_fraction)
        draw_frame(
            axis,
            view,
            config,
            title=(
                f"{condition.replace('--', ' · ')} · seed {row['seed']}\n"
                f"peak={view.largest_component_fraction:.3f} at t={view.time:.1f}"
            ),
        )
        selected[condition] = {
            "seed": int(row["seed"]),
            "frame": view.index,
            "time": view.time,
            "largest_component_fraction": view.largest_component_fraction,
        }
    figure.suptitle("Median-seed peak structures", fontsize=16)
    figure.savefig(output, dpi=180)
    plt.close(figure)
    return selected


def build_report(study_directory: Path) -> dict[str, Any]:
    rows = read_rows(study_directory / "runs.csv")
    report_directory = study_directory / "report"
    report_directory.mkdir(parents=True, exist_ok=True)
    representatives = representative_rows(rows)
    comparison = report_directory / "condition-comparison.png"
    energy = report_directory / "energy-comparison.png"
    peaks = report_directory / "peak-structures.png"
    comparison_figure(rows, comparison)
    energy_figure(representatives, energy)
    selected = peak_snapshot_figure(representatives, peaks)
    manifest = {
        "comparison": str(comparison.resolve()),
        "energy": str(energy.resolve()),
        "peaks": str(peaks.resolve()),
        "representatives": selected,
    }
    (report_directory / "report.json").write_text(
        json.dumps(manifest, indent=2) + "\n",
        encoding="utf-8",
    )
    return manifest
