from __future__ import annotations

from pathlib import Path

import numpy as np

from config import load_config, write_config
from metrics import component_sizes, contact_edges
from render import largest_component_nodes, select_frame_indices
from simulate import random_positions
from study import summarize_run


ROOT = Path(__file__).parents[1]


def test_configuration_declares_asymmetric_patch_types() -> None:
    config = load_config(ROOT / "experiment.toml")

    assert config.particle_count == 96
    assert [len(config.directors(name)) for name in config.particle_types] == [1, 2, 3]
    assert config.moment_of_inertia == 0.125
    assert config.attraction_for("P2", "P3") > config.attraction_for("P3", "P3")
    assert config.attraction_for("P1", "P2") > config.attraction_for("P1", "P1")


def test_component_sizes_include_isolated_particles() -> None:
    assert component_sizes(6, ((0, 1), (1, 2), (4, 5))) == (3, 2, 1)


def test_contact_graph_requires_facing_patches() -> None:
    config = load_config(ROOT / "experiment.toml")
    positions = np.asarray(((0.0, 0.0, 0.0), (1.2, 0.0, 0.0)))
    facing = np.asarray(((1.0, 0.0, 0.0, 0.0), (0.0, 0.0, 0.0, 1.0)))
    away = np.asarray(((1.0, 0.0, 0.0, 0.0), (1.0, 0.0, 0.0, 0.0)))

    assert contact_edges(positions, facing, (0, 0), ("P1",), config) == ((0, 1),)
    assert contact_edges(positions, away, (0, 0), ("P1",), config) == ()


def test_snapshot_selection_includes_peak_and_temporal_landmarks() -> None:
    fractions = [0.01] * 20
    fractions[7] = 0.8

    selected = select_frame_indices(20, fractions)

    assert selected == (0, 5, 10, 14, 7, 19)


def test_largest_component_nodes_returns_membership() -> None:
    assert largest_component_nodes(6, ((0, 1), (1, 2), (4, 5))) == frozenset(
        (0, 1, 2)
    )


def test_blue_noise_initialization_is_reproducible_and_spaced() -> None:
    config = load_config(ROOT / "experiment.toml")
    first = random_positions(config)
    second = random_positions(config)
    pair_distances = np.linalg.norm(
        first[:, np.newaxis, :2] - first[np.newaxis, :, :2],
        axis=2,
    )
    pair_distances += np.eye(config.particle_count) * config.box_length

    assert np.array_equal(first, second)
    assert float(np.min(pair_distances)) >= config.minimum_initial_distance


def test_resolved_configuration_round_trip(tmp_path: Path) -> None:
    config = load_config(ROOT / "experiment.toml")
    path = tmp_path / "resolved.toml"

    write_config(config, path)

    assert load_config(path) == config


def test_run_summary_separates_peak_tail_and_persistence() -> None:
    rows = [
        {
            "time": float(index),
            "largest_component_fraction": component,
            "mean_degree": float(index),
            "orientational_order": 0.1,
            "kinetic_temperature": 0.25,
            "potential_energy": -float(index),
            "kinetic_energy": float(index),
        }
        for index, component in enumerate((0.05, 0.20, 0.10, 0.05))
    ]

    summary = summarize_run(
        rows,
        tail_fraction=0.5,
        persistence_threshold=0.1,
    )

    assert summary["maximum_largest_component_fraction"] == 0.20
    assert summary["peak_time"] == 1.0
    assert np.isclose(summary["tail_largest_component_fraction"], 0.075)
    assert summary["persistence_fraction"] == 0.5
