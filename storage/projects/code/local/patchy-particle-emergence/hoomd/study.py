"""Run the bounded 2×2 × 3-seed HOOMD emergence study."""

from __future__ import annotations

import argparse
import csv
from dataclasses import asdict, replace
import hashlib
import json
import math
from pathlib import Path
import statistics
import tomllib

from analyze import analyze
from config import load_config, write_config
from simulate import run
from study_report import build_report


def read_observables(path: Path) -> list[dict[str, float]]:
    with path.open(newline="", encoding="utf-8") as stream:
        return [
            {name: float(value) for name, value in row.items()}
            for row in csv.DictReader(stream)
        ]


def summarize_run(
    rows: list[dict[str, float]],
    *,
    tail_fraction: float,
    persistence_threshold: float,
) -> dict[str, float]:
    tail_count = max(1, math.ceil(len(rows) * tail_fraction))
    tail = rows[-tail_count:]
    peak = max(rows, key=lambda row: row["largest_component_fraction"])

    def mean(items: list[dict[str, float]], field: str) -> float:
        return statistics.fmean(item[field] for item in items)

    return {
        "maximum_largest_component_fraction": peak[
            "largest_component_fraction"
        ],
        "peak_time": peak["time"],
        "tail_largest_component_fraction": mean(
            tail, "largest_component_fraction"
        ),
        "tail_mean_degree": mean(tail, "mean_degree"),
        "tail_orientational_order": mean(tail, "orientational_order"),
        "tail_kinetic_temperature": mean(tail, "kinetic_temperature"),
        "tail_potential_energy": mean(tail, "potential_energy"),
        "tail_kinetic_energy": mean(tail, "kinetic_energy"),
        "persistence_fraction": statistics.fmean(
            row["largest_component_fraction"] >= persistence_threshold
            for row in rows
        ),
    }


def write_csv(path: Path, rows: list[dict[str, object]]) -> None:
    with path.open("w", newline="", encoding="utf-8") as stream:
        writer = csv.DictWriter(stream, fieldnames=list(rows[0]))
        writer.writeheader()
        writer.writerows(rows)


def aggregate_conditions(rows: list[dict[str, object]]) -> list[dict[str, object]]:
    metric_names = (
        "maximum_largest_component_fraction",
        "tail_largest_component_fraction",
        "tail_mean_degree",
        "tail_orientational_order",
        "tail_kinetic_temperature",
        "tail_potential_energy",
        "tail_kinetic_energy",
        "persistence_fraction",
    )
    result: list[dict[str, object]] = []
    for condition in dict.fromkeys(str(row["condition"]) for row in rows):
        group = [row for row in rows if row["condition"] == condition]
        summary: dict[str, object] = {
            "condition": condition,
            "initialization": group[0]["initialization"],
            "chemistry": group[0]["chemistry"],
            "runs": len(group),
        }
        for metric in metric_names:
            values = [float(row[metric]) for row in group]
            summary[f"{metric}_mean"] = statistics.fmean(values)
            summary[f"{metric}_sd"] = (
                statistics.stdev(values) if len(values) > 1 else 0.0
            )
        result.append(summary)
    return result


def run_study(study_path: Path, output: Path, *, force: bool = False) -> None:
    with study_path.open("rb") as stream:
        raw = tomllib.load(stream)
    specification = raw["study"]
    base_path = study_path.parent / specification["base_config"]
    base = load_config(base_path)
    seeds = [int(seed) for seed in specification["seeds"]]
    tail_fraction = float(specification["tail_fraction"])
    persistence_threshold = float(specification["persistence_threshold"])
    output.mkdir(parents=True, exist_ok=True)

    run_rows: list[dict[str, object]] = []
    for initialization_name, initialization in raw["initializations"].items():
        for chemistry_name, chemistry in raw["chemistries"].items():
            condition = f"{initialization_name}--{chemistry_name}"
            pairs = {
                str(pair): float(value)
                for pair, value in chemistry.get("pairs", {}).items()
            }
            for seed in seeds:
                config = replace(
                    base,
                    seed=seed,
                    initialization_method=str(initialization["method"]),
                    candidate_pool=int(initialization["candidate_pool"]),
                    pair_attraction=pairs,
                )
                run_directory = output / condition / f"seed-{seed:04d}"
                run_directory.mkdir(parents=True, exist_ok=True)
                config_path = run_directory / "resolved.toml"
                write_config(config, config_path)
                checksum = hashlib.sha256(config_path.read_bytes()).hexdigest()
                run_manifest_path = run_directory / "study-run.json"
                reusable = False
                if not force and run_manifest_path.exists():
                    prior = json.loads(run_manifest_path.read_text(encoding="utf-8"))
                    reusable = (
                        prior.get("configuration_sha256") == checksum
                        and (run_directory / "summary.json").exists()
                        and (run_directory / "observables.csv").exists()
                        and (run_directory / "trajectory.gsd").exists()
                    )
                print(f"[{condition}] seed={seed} {'reuse' if reusable else 'run'}")
                if not reusable:
                    run(config_path, run_directory)
                    analyze(
                        config_path,
                        run_directory / "trajectory.gsd",
                        run_directory,
                    )
                    run_manifest_path.write_text(
                        json.dumps(
                            {
                                "condition": condition,
                                "initialization": initialization_name,
                                "chemistry": chemistry_name,
                                "seed": seed,
                                "configuration_sha256": checksum,
                                "parameters": asdict(config),
                            },
                            indent=2,
                        )
                        + "\n",
                        encoding="utf-8",
                    )
                observations = read_observables(run_directory / "observables.csv")
                run_rows.append(
                    {
                        "condition": condition,
                        "initialization": initialization_name,
                        "chemistry": chemistry_name,
                        "seed": seed,
                        "configuration_sha256": checksum,
                        "config": str(config_path.resolve()),
                        "trajectory": str((run_directory / "trajectory.gsd").resolve()),
                        "observables": str((run_directory / "observables.csv").resolve()),
                        **summarize_run(
                            observations,
                            tail_fraction=tail_fraction,
                            persistence_threshold=persistence_threshold,
                        ),
                    }
                )

    write_csv(output / "runs.csv", run_rows)
    condition_rows = aggregate_conditions(run_rows)
    write_csv(output / "conditions.csv", condition_rows)
    manifest = {
        "study": str(study_path.resolve()),
        "base_config": str(base_path.resolve()),
        "conditions": len(condition_rows),
        "seeds": seeds,
        "runs": len(run_rows),
        "tail_fraction": tail_fraction,
        "persistence_threshold": persistence_threshold,
    }
    (output / "study.json").write_text(
        json.dumps(manifest, indent=2) + "\n",
        encoding="utf-8",
    )
    report = build_report(output)
    print(json.dumps({**manifest, "report": report}, indent=2))


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--study", type=Path, default=Path("study.toml"))
    parser.add_argument("--output", type=Path, default=Path("outputs/study"))
    parser.add_argument("--force", action="store_true")
    return parser.parse_args()


if __name__ == "__main__":
    arguments = parse_args()
    run_study(arguments.study, arguments.output, force=arguments.force)

