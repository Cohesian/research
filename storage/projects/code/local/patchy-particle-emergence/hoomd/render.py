"""Render structural snapshots from a saved HOOMD trajectory."""

from __future__ import annotations

import argparse
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Sequence

import matplotlib.pyplot as plt
from matplotlib.lines import Line2D
from matplotlib.patches import Circle
import numpy as np

from config import ExperimentConfig, load_config
from metrics import (
    contact_edges,
    quaternion_angles,
    rotated_directors,
    structural_observables,
)


TYPE_COLORS = {
    "P1": "#66c2a5",
    "P2": "#8da0cb",
    "P3": "#fc8d62",
}


@dataclass(frozen=True)
class FrameView:
    index: int
    timestep: int
    time: float
    positions: np.ndarray
    orientations: np.ndarray
    type_ids: np.ndarray
    type_names: tuple[str, ...]
    largest_component_fraction: float


def select_frame_indices(
    frame_count: int,
    largest_component_fractions: Sequence[float],
) -> tuple[int, ...]:
    """Choose temporal landmarks and the strongest observed assembly event."""

    if frame_count < 1:
        raise ValueError("trajectory must contain at least one frame")
    if len(largest_component_fractions) != frame_count:
        raise ValueError("one cluster fraction is required for every frame")
    landmarks = (
        0,
        round((frame_count - 1) * 0.25),
        round((frame_count - 1) * 0.50),
        round((frame_count - 1) * 0.75),
        int(np.argmax(largest_component_fractions)),
        frame_count - 1,
    )
    return tuple(dict.fromkeys(landmarks))


def largest_component_nodes(
    particle_count: int,
    edges: Sequence[tuple[int, int]],
) -> frozenset[int]:
    adjacency = [set() for _ in range(particle_count)]
    for left, right in edges:
        adjacency[left].add(right)
        adjacency[right].add(left)
    remaining = set(range(particle_count))
    components: list[frozenset[int]] = []
    while remaining:
        start = remaining.pop()
        component = {start}
        frontier = [start]
        while frontier:
            node = frontier.pop()
            unseen = adjacency[node] & remaining
            remaining.difference_update(unseen)
            component.update(unseen)
            frontier.extend(unseen)
        components.append(frozenset(component))
    return max(components, key=len)


def frame_view(frame: Any, index: int, config: ExperimentConfig) -> FrameView:
    positions = np.asarray(frame.particles.position, dtype=float)
    orientations = np.asarray(frame.particles.orientation, dtype=float)
    type_ids = np.asarray(frame.particles.typeid, dtype=int)
    type_names = tuple(frame.particles.types)
    observables = structural_observables(
        positions,
        orientations,
        type_ids,
        type_names,
        config,
    )
    timestep = int(frame.configuration.step)
    return FrameView(
        index=index,
        timestep=timestep,
        time=timestep * config.dt,
        positions=positions,
        orientations=orientations,
        type_ids=type_ids,
        type_names=type_names,
        largest_component_fraction=observables["largest_component_fraction"],
    )


def draw_frame(
    axis: Any,
    view: FrameView,
    config: ExperimentConfig,
    *,
    title: str,
) -> None:
    edges = contact_edges(
        view.positions,
        view.orientations,
        view.type_ids,
        view.type_names,
        config,
    )
    largest_component = largest_component_nodes(len(view.positions), edges)
    for left, right in edges:
        highlighted = left in largest_component and right in largest_component
        axis.plot(
            view.positions[[left, right], 0],
            view.positions[[left, right], 1],
            color="#674ea7" if highlighted else "#46515f",
            linewidth=2.0 if highlighted else 0.9,
            alpha=0.85 if highlighted else 0.4,
            zorder=1,
        )

    angles = quaternion_angles(view.orientations)
    for index, (position, type_id, angle) in enumerate(
        zip(view.positions, view.type_ids, angles, strict=True)
    ):
        particle_type = view.type_names[int(type_id)]
        color = TYPE_COLORS.get(particle_type, "#b3b3b3")
        axis.add_patch(
            Circle(
                position[:2],
                radius=config.particle_radius,
                facecolor=color,
                edgecolor="#674ea7" if index in largest_component else "#222831",
                linewidth=1.55 if index in largest_component else 0.65,
                zorder=2,
            )
        )
        directors = rotated_directors(config, particle_type, float(angle))
        for director in directors:
            tip = position[:2] + config.particle_radius * director
            inner = position[:2] + 0.45 * config.particle_radius * director
            axis.plot(
                (inner[0], tip[0]),
                (inner[1], tip[1]),
                color="#1d2733",
                linewidth=1.0,
                zorder=3,
            )
            axis.scatter(
                tip[0],
                tip[1],
                s=5,
                color="#1d2733",
                zorder=4,
            )

    bound = config.wall_half_extent
    axis.set(
        xlim=(-bound, bound),
        ylim=(-bound, bound),
        aspect="equal",
        xticks=(),
        yticks=(),
        title=title,
    )
    for spine in axis.spines.values():
        spine.set_color("#727b86")
        spine.set_linewidth(1.2)


def render(
    config_path: Path,
    trajectory_path: Path,
    output_directory: Path,
) -> None:
    try:
        import gsd.hoomd
    except ImportError as error:
        raise SystemExit(
            "The GSD package is missing. Run through Pixi: `pixi run render`."
        ) from error

    config = load_config(config_path)
    output_directory.mkdir(parents=True, exist_ok=True)
    snapshot_directory = output_directory / "snapshots"
    snapshot_directory.mkdir(parents=True, exist_ok=True)

    with gsd.hoomd.open(name=str(trajectory_path), mode="r") as trajectory:
        views = [frame_view(frame, index, config) for index, frame in enumerate(trajectory)]
    fractions = [view.largest_component_fraction for view in views]
    selected = select_frame_indices(len(views), fractions)
    strongest = int(np.argmax(fractions))

    columns = 3
    rows = int(np.ceil(len(selected) / columns))
    figure, axes = plt.subplots(
        rows,
        columns,
        figsize=(12, 4.15 * rows),
        constrained_layout=True,
        squeeze=False,
    )
    for axis, index in zip(axes.flat, selected, strict=False):
        view = views[index]
        label = "maximum cluster" if index == strongest else f"frame {index}"
        draw_frame(
            axis,
            view,
            config,
            title=(
                f"{label} · t={view.time:.1f}\n"
                f"largest component={view.largest_component_fraction:.3f}"
            ),
        )
        individual, individual_axis = plt.subplots(figsize=(6, 6), constrained_layout=True)
        draw_frame(
            individual_axis,
            view,
            config,
            title=(
                f"t={view.time:.1f} · "
                f"largest component={view.largest_component_fraction:.3f}"
            ),
        )
        individual.savefig(
            snapshot_directory / f"frame-{index:04d}-t-{view.time:.1f}.png",
            dpi=180,
        )
        plt.close(individual)
    for axis in axes.flat[len(selected) :]:
        axis.remove()

    legend = [
        Line2D(
            [0],
            [0],
            marker="o",
            color="none",
            markerfacecolor=TYPE_COLORS.get(name, "#b3b3b3"),
            markeredgecolor="#222831",
            markersize=9,
            label=f"{name}: {config.patch_count(name)} patch(es)",
        )
        for name in config.particle_types
    ]
    legend.append(
        Line2D([0], [0], color="#46515f", linewidth=1.5, label="patch contact")
    )
    legend.append(
        Line2D(
            [0],
            [0],
            color="#674ea7",
            linewidth=2.5,
            label="largest component",
        )
    )
    figure.legend(handles=legend, loc="outside lower center", ncol=len(legend))
    figure.suptitle("Cohesian emergence — structural trajectory snapshots", fontsize=16)
    output_path = output_directory / "snapshots.png"
    figure.savefig(output_path, dpi=180)
    plt.close(figure)
    print(f"snapshot montage: {output_path}")
    print(f"individual snapshots: {snapshot_directory}")


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
    render(arguments.config, arguments.trajectory, arguments.output)
