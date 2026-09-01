"""Project a HOOMD trajectory into thermodynamic and structural observables."""

from __future__ import annotations

import argparse
import csv
import json
from pathlib import Path
from typing import Any

import matplotlib.pyplot as plt
import numpy as np

from config import load_config
from metrics import structural_observables


THERMODYNAMIC_FIELDS = (
    "kinetic_temperature",
    "kinetic_energy",
    "translational_kinetic_energy",
    "rotational_kinetic_energy",
    "potential_energy",
    "pressure",
)


def scalar_log(frame: Any, quantity: str) -> float:
    log = frame.log or {}
    matches = [name for name in log if name.endswith(f"/{quantity}")]
    if not matches:
        return float("nan")
    value = np.asarray(log[matches[0]], dtype=float).squeeze()
    return float(value)


def analyze(
    config_path: Path,
    trajectory_path: Path,
    output_directory: Path,
) -> dict[str, object]:
    try:
        import gsd.hoomd
    except ImportError as error:
        raise SystemExit(
            "The GSD package is missing. Run this analysis through Pixi: "
            "`pixi run analyze`."
        ) from error

    config = load_config(config_path)
    output_directory.mkdir(parents=True, exist_ok=True)
    rows: list[dict[str, float]] = []
    with gsd.hoomd.open(name=str(trajectory_path), mode="r") as trajectory:
        for frame in trajectory:
            row = {
                "timestep": float(frame.configuration.step),
                "time": float(frame.configuration.step * config.dt),
                **{
                    field: scalar_log(frame, field)
                    for field in THERMODYNAMIC_FIELDS
                },
                **structural_observables(
                    np.asarray(frame.particles.position, dtype=float),
                    np.asarray(frame.particles.orientation, dtype=float),
                    frame.particles.typeid,
                    frame.particles.types,
                    config,
                ),
            }
            rows.append(row)
    if not rows:
        raise RuntimeError(f"trajectory contains no frames: {trajectory_path}")

    csv_path = output_directory / "observables.csv"
    with csv_path.open("w", newline="", encoding="utf-8") as stream:
        writer = csv.DictWriter(stream, fieldnames=list(rows[0]))
        writer.writeheader()
        writer.writerows(rows)

    times = np.asarray([row["time"] for row in rows])
    figure, axes = plt.subplots(2, 2, figsize=(11, 7), constrained_layout=True)
    axes[0, 0].plot(times, [row["potential_energy"] for row in rows], label="U")
    axes[0, 0].plot(times, [row["kinetic_energy"] for row in rows], label="K")
    axes[0, 0].set(title="Energy", xlabel="time", ylabel="reduced energy")
    axes[0, 0].legend()
    axes[0, 1].plot(times, [row["kinetic_temperature"] for row in rows])
    axes[0, 1].axhline(config.temperature, color="black", linestyle="--", alpha=0.5)
    axes[0, 1].set(title="Kinetic temperature", xlabel="time", ylabel="kT")
    axes[1, 0].plot(
        times,
        [row["largest_component_fraction"] for row in rows],
    )
    axes[1, 0].set(
        title="Largest patch-contact component",
        xlabel="time",
        ylabel="fraction of particles",
        ylim=(0.0, 1.05),
    )
    axes[1, 1].plot(times, [row["mean_degree"] for row in rows], label="degree")
    axes[1, 1].plot(
        times,
        [row["orientational_order"] for row in rows],
        label=f"|psi_{config.orientational_order}|",
    )
    axes[1, 1].set(title="Structural order", xlabel="time")
    axes[1, 1].legend()
    figure.suptitle("Cohesian emergence — HOOMD benchmark")
    figure_path = output_directory / "observables.png"
    figure.savefig(figure_path, dpi=180)
    plt.close(figure)

    summary = {
        "frames": len(rows),
        "final_time": rows[-1]["time"],
        "final_largest_component_fraction": rows[-1][
            "largest_component_fraction"
        ],
        "maximum_largest_component_fraction": max(
            row["largest_component_fraction"] for row in rows
        ),
        "final_mean_degree": rows[-1]["mean_degree"],
        "final_orientational_order": rows[-1]["orientational_order"],
        "observables": str(csv_path.resolve()),
        "figure": str(figure_path.resolve()),
    }
    (output_directory / "summary.json").write_text(
        json.dumps(summary, indent=2) + "\n",
        encoding="utf-8",
    )
    print(json.dumps(summary, indent=2))
    return summary


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--config", type=Path, default=Path("experiment.toml"))
    parser.add_argument(
        "--trajectory",
        type=Path,
        default=Path("outputs/trajectory.gsd"),
    )
    parser.add_argument("--output", type=Path, default=Path("outputs"))
    return parser.parse_args()


if __name__ == "__main__":
    arguments = parse_args()
    analyze(arguments.config, arguments.trajectory, arguments.output)
