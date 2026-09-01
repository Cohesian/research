"""Render one saved HOOMD trajectory as a compact emergence demonstration."""

from __future__ import annotations

import argparse
from dataclasses import dataclass
from pathlib import Path
from typing import Any

from matplotlib import animation
from matplotlib.collections import LineCollection
from matplotlib.lines import Line2D
import matplotlib.pyplot as plt
import numpy as np

from config import ExperimentConfig, load_config
from metrics import contact_edges, quaternion_angles, rotated_directors
from render import TYPE_COLORS, largest_component_nodes


BACKGROUND = "#0f131a"
PANEL = "#171d27"
TEXT = "#eef2f7"
MUTED = "#93a1b2"
GRID = "#303a49"
CONTACT = "#536172"
HIGHLIGHT = "#a78bfa"
ACCENT = "#ef8354"


@dataclass(frozen=True)
class AnimationFrame:
    time: float
    positions: np.ndarray
    angles: np.ndarray
    type_ids: np.ndarray
    type_names: tuple[str, ...]
    edges: tuple[tuple[int, int], ...]
    largest_component: frozenset[int]
    largest_fraction: float
    mean_degree: float
    orientational_order: float


def load_frames(
    trajectory_path: Path,
    config: ExperimentConfig,
) -> list[AnimationFrame]:
    try:
        import gsd.hoomd
    except ImportError as error:
        raise SystemExit(
            "The GSD package is missing. Run this command through Pixi."
        ) from error

    frames: list[AnimationFrame] = []
    with gsd.hoomd.open(name=str(trajectory_path), mode="r") as trajectory:
        for frame in trajectory:
            positions = np.asarray(frame.particles.position, dtype=float).copy()
            orientations = np.asarray(frame.particles.orientation, dtype=float)
            angles = quaternion_angles(orientations)
            type_ids = np.asarray(frame.particles.typeid, dtype=int).copy()
            type_names = tuple(frame.particles.types)
            edges = contact_edges(
                positions,
                orientations,
                type_ids,
                type_names,
                config,
            )
            component = largest_component_nodes(len(positions), edges)
            order = abs(
                np.mean(np.exp(1j * config.orientational_order * angles))
            )
            frames.append(
                AnimationFrame(
                    time=float(frame.configuration.step) * config.dt,
                    positions=positions,
                    angles=angles,
                    type_ids=type_ids,
                    type_names=type_names,
                    edges=edges,
                    largest_component=component,
                    largest_fraction=len(component) / len(positions),
                    mean_degree=2.0 * len(edges) / len(positions),
                    orientational_order=float(order),
                )
            )
    if not frames:
        raise ValueError("trajectory contains no frames")
    return frames


def patch_segments(
    frame: AnimationFrame,
    config: ExperimentConfig,
) -> list[np.ndarray]:
    segments: list[np.ndarray] = []
    for position, type_id, angle in zip(
        frame.positions,
        frame.type_ids,
        frame.angles,
        strict=True,
    ):
        particle_type = frame.type_names[int(type_id)]
        for director in rotated_directors(config, particle_type, float(angle)):
            segments.append(
                np.asarray(
                    (
                        position[:2] + 0.38 * config.particle_radius * director,
                        position[:2] + config.particle_radius * director,
                    )
                )
            )
    return segments


def edge_segments(
    frame: AnimationFrame,
    *,
    highlighted: bool,
) -> list[np.ndarray]:
    segments: list[np.ndarray] = []
    for left, right in frame.edges:
        in_component = (
            left in frame.largest_component and right in frame.largest_component
        )
        if in_component == highlighted:
            segments.append(frame.positions[[left, right], :2])
    return segments


def frame_sequence(frame_count: int, peak_index: int, fps: int) -> list[int]:
    sequence: list[int] = [0] * round(0.5 * fps)
    for index in range(frame_count):
        sequence.append(index)
        if index == peak_index:
            sequence.extend([index] * round(0.8 * fps))
    sequence.extend([frame_count - 1] * round(0.8 * fps))
    return sequence


def render_animation(
    config_path: Path,
    trajectory_path: Path,
    output_path: Path,
    *,
    fps: int,
    dpi: int,
) -> None:
    config = load_config(config_path)
    frames = load_frames(trajectory_path, config)
    fractions = np.asarray([frame.largest_fraction for frame in frames])
    times = np.asarray([frame.time for frame in frames])
    peak_index = int(np.argmax(fractions))
    sequence = frame_sequence(len(frames), peak_index, fps)

    figure = plt.figure(figsize=(12.8, 7.2), facecolor=BACKGROUND)
    grid = figure.add_gridspec(
        2,
        2,
        width_ratios=(1.45, 0.72),
        height_ratios=(1.0, 0.34),
        left=0.045,
        right=0.97,
        bottom=0.075,
        top=0.92,
        wspace=0.12,
        hspace=0.15,
    )
    system_axis = figure.add_subplot(grid[:, 0])
    information_axis = figure.add_subplot(grid[0, 1])
    timeline_axis = figure.add_subplot(grid[1, 1])

    for axis in (system_axis, information_axis, timeline_axis):
        axis.set_facecolor(PANEL)
    figure.suptitle(
        "Emergence from local patch interactions",
        color=TEXT,
        fontsize=22,
        fontweight="bold",
        x=0.045,
        ha="left",
    )

    bound = config.wall_half_extent
    system_axis.set(
        xlim=(-bound, bound),
        ylim=(-bound, bound),
        aspect="equal",
        xticks=(),
        yticks=(),
    )
    for spine in system_axis.spines.values():
        spine.set_color(GRID)
        spine.set_linewidth(1.2)

    first = frames[0]
    colors = [
        TYPE_COLORS.get(first.type_names[int(type_id)], "#b3b3b3")
        for type_id in first.type_ids
    ]
    particles = system_axis.scatter(
        first.positions[:, 0],
        first.positions[:, 1],
        s=280,
        facecolors=colors,
        edgecolors="#28313d",
        linewidths=0.85,
        zorder=3,
    )
    patch_lines = LineCollection(
        patch_segments(first, config),
        colors="#111820",
        linewidths=1.6,
        zorder=4,
    )
    ordinary_edges = LineCollection(
        [],
        colors=CONTACT,
        linewidths=1.1,
        alpha=0.55,
        zorder=1,
    )
    highlighted_edges = LineCollection(
        [],
        colors=HIGHLIGHT,
        linewidths=3.2,
        alpha=0.95,
        zorder=2,
    )
    system_axis.add_collection(ordinary_edges)
    system_axis.add_collection(highlighted_edges)
    system_axis.add_collection(patch_lines)

    information_axis.set_axis_off()
    information_axis.text(
        0.04,
        0.94,
        "LOCAL RULES",
        color=ACCENT,
        fontsize=11,
        fontweight="bold",
        transform=information_axis.transAxes,
    )
    information_axis.text(
        0.04,
        0.84,
        "repel overlap\nrotate and translate\nattract aligned patches",
        color=TEXT,
        fontsize=14,
        linespacing=1.45,
        transform=information_axis.transAxes,
        va="top",
    )
    information_axis.text(
        0.04,
        0.56,
        "No particle receives a target shape.",
        color=MUTED,
        fontsize=11.5,
        transform=information_axis.transAxes,
    )
    time_text = information_axis.text(
        0.04,
        0.42,
        "",
        color=TEXT,
        fontsize=15,
        fontweight="bold",
        transform=information_axis.transAxes,
    )
    component_text = information_axis.text(
        0.04,
        0.35,
        "",
        color=HIGHLIGHT,
        fontsize=18,
        fontweight="bold",
        va="top",
        transform=information_axis.transAxes,
    )
    metrics_text = information_axis.text(
        0.04,
        0.23,
        "",
        color=MUTED,
        fontsize=12,
        linespacing=1.45,
        va="top",
        transform=information_axis.transAxes,
    )
    peak_text = information_axis.text(
        0.04,
        0.04,
        "",
        color=ACCENT,
        fontsize=11,
        fontweight="bold",
        transform=information_axis.transAxes,
    )

    legend = [
        Line2D(
            [0],
            [0],
            marker="o",
            linestyle="none",
            markerfacecolor=TYPE_COLORS[name],
            markeredgecolor="#28313d",
            markersize=9,
            label=(
                f"{name} · {config.patch_count(name)} "
                f"{'patch' if config.patch_count(name) == 1 else 'patches'}"
            ),
        )
        for name in config.particle_types
    ]
    legend.append(
        Line2D(
            [0],
            [0],
            color=HIGHLIGHT,
            linewidth=3,
            label="largest component",
        )
    )
    system_axis.legend(
        handles=legend,
        loc="upper left",
        ncol=2,
        frameon=False,
        labelcolor=TEXT,
        fontsize=9.5,
        borderaxespad=0.8,
    )

    timeline_axis.plot(times, fractions, color=GRID, linewidth=1.5)
    active_line, = timeline_axis.plot([], [], color=ACCENT, linewidth=2.4)
    current_point, = timeline_axis.plot([], [], "o", color=HIGHLIGHT, markersize=6)
    timeline_axis.axvline(
        times[peak_index],
        color=HIGHLIGHT,
        linewidth=1,
        alpha=0.35,
    )
    timeline_axis.set(
        xlim=(times[0], times[-1]),
        ylim=(0, max(0.18, float(np.max(fractions)) * 1.18)),
        xlabel="simulated time",
        ylabel="$S_{max}$",
    )
    timeline_axis.tick_params(colors=MUTED, labelsize=8)
    timeline_axis.xaxis.label.set_color(MUTED)
    timeline_axis.yaxis.label.set_color(MUTED)
    timeline_axis.grid(color=GRID, alpha=0.35, linewidth=0.7)
    for spine in timeline_axis.spines.values():
        spine.set_color(GRID)

    def update(source_index: int) -> tuple[Any, ...]:
        frame = frames[source_index]
        particles.set_offsets(frame.positions[:, :2])
        edge_colors = np.asarray(
            [
                HIGHLIGHT if index in frame.largest_component else "#28313d"
                for index in range(len(frame.positions))
            ]
        )
        line_widths = np.asarray(
            [
                1.9 if index in frame.largest_component else 0.85
                for index in range(len(frame.positions))
            ]
        )
        particles.set_edgecolors(edge_colors)
        particles.set_linewidths(line_widths)
        patch_lines.set_segments(patch_segments(frame, config))
        ordinary_edges.set_segments(edge_segments(frame, highlighted=False))
        highlighted_edges.set_segments(edge_segments(frame, highlighted=True))

        component_size = len(frame.largest_component)
        time_text.set_text(f"t = {frame.time:6.1f} / {frames[-1].time:.1f}")
        component_text.set_text(
            f"largest structure  {component_size}/{len(frame.positions)}"
        )
        metrics_text.set_text(
            f"connected fraction   {frame.largest_fraction:.3f}\n"
            f"mean contact degree  {frame.mean_degree:.3f}\n"
            f"orientational order  {frame.orientational_order:.3f}"
        )
        peak_text.set_text(
            "STRONGEST OBSERVED ASSEMBLY" if source_index == peak_index else ""
        )
        active_line.set_data(times[: source_index + 1], fractions[: source_index + 1])
        current_point.set_data([frame.time], [frame.largest_fraction])
        return (
            particles,
            patch_lines,
            ordinary_edges,
            highlighted_edges,
            time_text,
            component_text,
            metrics_text,
            peak_text,
            active_line,
            current_point,
        )

    movie = animation.FuncAnimation(
        figure,
        update,
        frames=sequence,
        interval=1000 / fps,
        blit=False,
        repeat=False,
    )
    output_path.parent.mkdir(parents=True, exist_ok=True)
    writer = animation.FFMpegWriter(
        fps=fps,
        codec="libx264",
        extra_args=(
            "-crf",
            "20",
            "-preset",
            "medium",
            "-pix_fmt",
            "yuv420p",
            "-movflags",
            "+faststart",
        ),
    )
    movie.save(output_path, writer=writer, dpi=dpi)
    plt.close(figure)
    print(f"video: {output_path}")
    print(f"source frames: {len(frames)}")
    print(f"encoded frames: {len(sequence)}")
    print(f"duration: {len(sequence) / fps:.2f} seconds")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--config", type=Path, required=True)
    parser.add_argument("--trajectory", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--fps", type=int, default=30)
    parser.add_argument("--dpi", type=int, default=150)
    return parser.parse_args()


if __name__ == "__main__":
    arguments = parse_args()
    render_animation(
        arguments.config,
        arguments.trajectory,
        arguments.output,
        fps=arguments.fps,
        dpi=arguments.dpi,
    )
