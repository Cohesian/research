"""Run the fixed-patch HOOMD molecular-dynamics benchmark."""

from __future__ import annotations

import argparse
from dataclasses import replace
from itertools import combinations_with_replacement
import json
import math
from pathlib import Path

import numpy as np

from config import ExperimentConfig, load_config


def random_positions(config: ExperimentConfig) -> np.ndarray:
    """Place particles inside the barriers using the configured sampler."""

    rng = np.random.default_rng(config.seed)
    margin = config.particle_radius + 0.15
    bound = config.wall_half_extent - margin
    positions: list[np.ndarray] = []
    attempts = 0
    maximum_attempts = max(10000, config.particle_count * 1000)
    while len(positions) < config.particle_count:
        attempts += 1
        if attempts > maximum_attempts:
            raise RuntimeError(
                "could not create a non-overlapping initial state; "
                "increase the box or reduce the population"
            )
        if config.initialization_method == "uniform_rejection" or not positions:
            candidates = rng.uniform(-bound, bound, size=(1, 2))
        else:
            candidates = rng.uniform(
                -bound,
                bound,
                size=(config.candidate_pool, 2),
            )
        if not positions:
            positions.append(candidates[0])
            continue
        existing = np.asarray(positions)
        distances = np.linalg.norm(
            candidates[:, np.newaxis, :] - existing[np.newaxis, :, :],
            axis=2,
        )
        nearest = np.min(distances, axis=1)
        best = int(np.argmax(nearest))
        if nearest[best] >= config.minimum_initial_distance:
            positions.append(candidates[best])
    return np.column_stack((np.asarray(positions), np.zeros(len(positions))))


def type_ids(config: ExperimentConfig) -> np.ndarray:
    values: list[int] = []
    for type_id, particle_type in enumerate(config.particle_types):
        values.extend([type_id] * config.population[particle_type])
    rng = np.random.default_rng(config.seed + 1)
    result = np.asarray(values, dtype=np.uint32)
    rng.shuffle(result)
    return result


def orientations(config: ExperimentConfig) -> np.ndarray:
    rng = np.random.default_rng(config.seed + 2)
    angles = rng.uniform(-math.pi, math.pi, size=config.particle_count)
    return np.column_stack(
        (
            np.cos(angles / 2.0),
            np.zeros(config.particle_count),
            np.zeros(config.particle_count),
            np.sin(angles / 2.0),
        )
    )


def build_snapshot(hoomd: object, config: ExperimentConfig) -> object:
    snapshot = hoomd.Snapshot()
    if snapshot.communicator.rank == 0:
        snapshot.configuration.box = [
            config.box_length,
            config.box_length,
            0.0,
            0.0,
            0.0,
            0.0,
        ]
        snapshot.particles.N = config.particle_count
        snapshot.particles.types = list(config.particle_types)
        snapshot.particles.typeid[:] = type_ids(config)
        snapshot.particles.position[:] = random_positions(config)
        snapshot.particles.orientation[:] = orientations(config)
        snapshot.particles.mass[:] = config.particle_mass
        snapshot.particles.diameter[:] = config.particle_diameter
        snapshot.particles.moment_inertia[:] = (
            0.0,
            0.0,
            config.moment_of_inertia,
        )
    return snapshot


def configure_forces(hoomd: object, config: ExperimentConfig) -> list[object]:
    neighbor_list = hoomd.md.nlist.Cell(buffer=0.4)
    repulsive_cutoff = 2.0 ** (1.0 / 6.0) * config.particle_diameter
    repulsion = hoomd.md.pair.LJ(
        nlist=neighbor_list,
        default_r_cut=repulsive_cutoff,
        mode="shift",
    )
    attraction = hoomd.md.pair.aniso.PatchyGaussian(
        nlist=neighbor_list,
        default_r_cut=config.patch_cutoff,
        mode="shift",
    )
    envelope_params = {
        "alpha": config.patch_half_angle,
        "omega": config.patch_steepness,
    }
    for pair in combinations_with_replacement(config.particle_types, 2):
        repulsion.params[pair] = {
            "epsilon": config.repulsion_energy,
            "sigma": config.particle_diameter,
        }
        attraction.params[pair] = {
            "pair_params": {
                "epsilon": -config.attraction_for(*pair),
                "sigma": config.patch_range,
            },
            "envelope_params": envelope_params,
        }
    for particle_type in config.particle_types:
        attraction.directors[particle_type] = list(config.directors(particle_type))

    walls = [
        hoomd.wall.Plane(
            origin=(config.wall_half_extent, 0.0, 0.0),
            normal=(-1.0, 0.0, 0.0),
        ),
        hoomd.wall.Plane(
            origin=(-config.wall_half_extent, 0.0, 0.0),
            normal=(1.0, 0.0, 0.0),
        ),
        hoomd.wall.Plane(
            origin=(0.0, config.wall_half_extent, 0.0),
            normal=(0.0, -1.0, 0.0),
        ),
        hoomd.wall.Plane(
            origin=(0.0, -config.wall_half_extent, 0.0),
            normal=(0.0, 1.0, 0.0),
        ),
    ]
    wall_repulsion = hoomd.md.external.wall.LJ(walls=walls)
    for particle_type in config.particle_types:
        wall_repulsion.params[particle_type] = {
            "epsilon": config.repulsion_energy,
            "sigma": config.particle_diameter,
            "r_cut": repulsive_cutoff,
        }
    return [repulsion, attraction, wall_repulsion]


def run(
    config_path: Path,
    output_directory: Path,
    *,
    steps: int | None = None,
    write_period: int | None = None,
) -> None:
    try:
        import hoomd
    except ImportError as error:
        raise SystemExit(
            "HOOMD-blue is not installed in this Python environment. "
            "Run this experiment through Pixi: `pixi run simulate`."
        ) from error

    config = load_config(config_path)
    if steps is not None:
        config = replace(config, steps=steps)
    if write_period is not None:
        config = replace(config, write_period=write_period)
    config.validate()
    output_directory.mkdir(parents=True, exist_ok=True)
    trajectory_path = output_directory / "trajectory.gsd"

    simulation = hoomd.Simulation(device=hoomd.device.auto_select(), seed=config.seed)
    simulation.create_state_from_snapshot(build_snapshot(hoomd, config))

    langevin = hoomd.md.methods.Langevin(
        filter=hoomd.filter.All(),
        kT=config.temperature,
        default_gamma=config.linear_drag,
        default_gamma_r=(
            config.angular_drag,
            config.angular_drag,
            config.angular_drag,
        ),
    )
    forces = configure_forces(hoomd, config)
    simulation.operations.integrator = hoomd.md.Integrator(
        dt=config.dt,
        integrate_rotational_dof=True,
        methods=[langevin],
        forces=forces,
    )

    thermodynamics = hoomd.md.compute.ThermodynamicQuantities(
        filter=hoomd.filter.All()
    )
    simulation.operations.computes.append(thermodynamics)
    logger = hoomd.logging.Logger(categories=["scalar"])
    logger.add(simulation, quantities=["timestep", "tps"])
    logger.add(
        thermodynamics,
        quantities=[
            "kinetic_temperature",
            "kinetic_energy",
            "translational_kinetic_energy",
            "rotational_kinetic_energy",
            "potential_energy",
            "pressure",
        ],
    )
    writer = hoomd.write.GSD(
        trigger=hoomd.trigger.Periodic(config.write_period),
        filename=str(trajectory_path),
        mode="wb",
        filter=hoomd.filter.All(),
        dynamic=["property", "momentum"],
        logger=logger,
    )
    simulation.operations.writers.append(writer)

    simulation.run(0)
    simulation.state.thermalize_particle_momenta(
        filter=hoomd.filter.All(),
        kT=config.temperature,
    )
    simulation.run(config.steps)
    writer.flush()

    metadata = {
        "config": str(config_path.resolve()),
        "trajectory": str(trajectory_path.resolve()),
        "seed": config.seed,
        "dt": config.dt,
        "steps": config.steps,
        "simulated_time": config.dt * config.steps,
        "particle_count": config.particle_count,
        "population": config.population,
        "device": type(simulation.device).__name__,
    }
    (output_directory / "run.json").write_text(
        json.dumps(metadata, indent=2) + "\n",
        encoding="utf-8",
    )
    print(f"trajectory: {trajectory_path}")
    print(f"simulated time: {metadata['simulated_time']}")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--config", type=Path, default=Path("experiment.toml"))
    parser.add_argument("--output", type=Path, default=Path("outputs"))
    parser.add_argument("--steps", type=int)
    parser.add_argument("--write-period", type=int)
    return parser.parse_args()


if __name__ == "__main__":
    arguments = parse_args()
    run(
        arguments.config,
        arguments.output,
        steps=arguments.steps,
        write_period=arguments.write_period,
    )
