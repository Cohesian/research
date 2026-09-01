"""Build the controlled-study notebook from a reviewable Python source."""

from __future__ import annotations

from pathlib import Path

import nbformat as nbf


ROOT = Path(__file__).resolve().parent
NOTEBOOK = ROOT / "notebooks" / "02-controlled-emergence-study.ipynb"


def markdown(text: str):
    return nbf.v4.new_markdown_cell(text.strip())


def code(text: str):
    return nbf.v4.new_code_cell(text.strip())


def build() -> Path:
    notebook = nbf.v4.new_notebook()
    notebook["metadata"] = {
        "kernelspec": {
            "display_name": "Python 3 (Pixi)",
            "language": "python",
            "name": "python3",
        },
        "language_info": {"name": "python", "version": "3.12"},
    }
    notebook["cells"] = [
        markdown(
            r"""
# Controlled patchy-particle emergence study

This laboratory asks one bounded question: **can finite-range, directional
particle rules produce observable structures at a scale larger than one
interaction?** It compares two initialization methods and two type-affinity
rules while holding the remaining physical parameters fixed.

The notebook analyzes a seeded HOOMD-blue ensemble. It is not a claim about a
universal thermodynamic phase, an atomistic material, or quantum mechanics.
"""
        ),
        markdown(
            r"""
## From local state to global observation

The complete microscopic state is

$$
X(t)=\bigl(s_1(t),\ldots,s_N(t)\bigr).
$$

Each particle reacts only through finite-range pair interactions and the local
walls. An external observer then applies two projections:

$$
X(t)\xrightarrow{\Pi_G}G_t=(V,E_t)
\xrightarrow{\Pi_M}
\bigl(S_{\max},\langle k\rangle,\Psi_2,U,K,T_{\mathrm{kin}}\bigr)_t.
$$

The first projection produces an instantaneous contact graph. The second
produces macroscopic measurements. Neither projection is fed back into the
simulation, so observation does not become centralized control.
"""
        ),
        markdown(
            r"""
## Microscopic model

Particles have one, two, or three body-fixed patch directions. The conservative
energy is

$$
U(X)=\sum_{i<j}
\left[U_{\mathrm{WCA}}(r_{ij})
+U_{\mathrm{patch}}(r_{ij},q_i,q_j)\right]
+\sum_iU_{\mathrm{wall}}(\mathbf x_i).
$$

The WCA core resists overlap. A shifted radial Gaussian, multiplied by HOOMD's
angular patch masks, provides directional attraction and torque. Translation
follows Langevin dynamics,

$$
m\frac{d\mathbf v_i}{dt}
=\mathbf F_i^{\mathrm C}-\gamma\mathbf v_i+\mathbf F_i^{\mathrm R},
\qquad
\frac{d\mathbf x_i}{dt}=\mathbf v_i,
$$

with an analogous rotational equation. The heat bath therefore exchanges
energy with the particles; $U+K$ is not expected to be conserved.
"""
        ),
        markdown(
            r"""
## Experimental design

The controlled $2\times2$ design is

$$
\{\text{random},\text{blue-noise}\}
\times
\{\text{uniform},\text{selective}\}.
$$

Each condition is repeated for three seeds. The initialization axis tests
whether accidental initial crowding changes the observation. The chemistry
axis tests whether a symmetric type-pair attraction matrix changes assembly.
Particle counts, density, temperature, timestep, patch geometry, barriers,
and run length are shared by all conditions.
"""
        ),
        code(
            """
from pathlib import Path
import pandas as pd
from IPython.display import Image, display


def find_project(start: Path) -> Path:
    start = start.resolve()
    for root in (start, *start.parents):
        direct = root if (root / "study.toml").exists() else None
        nested = root / "experiments" / "emergence" / "hoomd"
        if direct is not None:
            return direct
        if (nested / "study.toml").exists():
            return nested
    raise FileNotFoundError("Could not locate the HOOMD study project.")


PROJECT = find_project(Path.cwd())
OUTPUT = PROJECT / "outputs" / "study"
RUNS = pd.read_csv(OUTPUT / "runs.csv")
CONDITIONS = pd.read_csv(OUTPUT / "conditions.csv")
print(f"project: {PROJECT}")
print(f"runs: {len(RUNS)}")
"""
        ),
        code(
            """
columns = [
    "condition",
    "runs",
    "maximum_largest_component_fraction_mean",
    "maximum_largest_component_fraction_sd",
    "tail_largest_component_fraction_mean",
    "tail_largest_component_fraction_sd",
    "tail_mean_degree_mean",
    "tail_orientational_order_mean",
]
CONDITIONS[columns].round(4)
"""
        ),
        markdown(
            r"""
## Structural projection

The simulation has continuous particle state. For analysis, every saved frame
is projected into a contact graph $G_t=(V,E_t)$. An edge is inferred only when
two particles are near and mutually patch-aligned. From this graph we measure

$$
S_{\max}(t)=\frac{\max_{C\in\operatorname{CC}(G_t)}|C|}{|V|},
\qquad
\langle k\rangle_t=\frac{2|E_t|}{|V|}.
$$

$S_{\max}$ measures the largest connected structure; mean degree measures its
local connectivity. These are analysis observables, not permanent HOOMD bonds.
"""
        ),
        code(
            """
display(Image(filename=str(OUTPUT / "report" / "condition-comparison.png"), width=1000))
"""
        ),
        markdown(
            r"""
## Representative peak structures

For each condition, the panel below uses the seed whose maximum component is
the median of the three seed maxima. The displayed frame is that run's peak,
not a hand-selected final state. Purple outlines and edges identify the
largest inferred contact component.
"""
        ),
        code(
            """
display(Image(filename=str(OUTPUT / "report" / "peak-structures.png"), width=1000))
"""
        ),
        markdown(
            r"""
## Energetic context

Potential energy $U$ and kinetic energy $K$ provide context for structural
change. Because the system uses a Langevin thermostat, neither quantity is
expected to remain constant: the bath exchanges energy with the particles.
The measured kinetic temperature should instead fluctuate around the declared
target.
"""
        ),
        code(
            """
display(Image(filename=str(OUTPUT / "report" / "energy-comparison.png"), width=1000))
"""
        ),
        code(
            """
target_temperature = 0.25
temperature_check = CONDITIONS[["condition", "tail_kinetic_temperature_mean"]].copy()
temperature_check["difference_from_target"] = (
    temperature_check["tail_kinetic_temperature_mean"] - target_temperature
)
temperature_check.round(4)
"""
        ),
        markdown(
            r"""
## What this ensemble supports

Within this finite experiment, selective type affinity increased the observed
peak connected fraction relative to uniform affinity for both initialization
methods. The blue-noise/selective condition had the most consistent peak
across the three seeds, while the random/selective condition had the greatest
seed variance and the highest single-run peak. Selective conditions also had
more negative mean tail potential energy.

The evidence therefore supports a modest statement: **changing only the local
type-affinity rule changed the distribution of finite structural observables**.
It does not yet establish a stable bulk phase, asymptotic scaling law, or
universality class. Three seeds and one finite system size are an exploratory
ensemble; larger seed counts, sizes, durations, and timestep checks belong to
a later study.
"""
        ),
        markdown(
            r"""
## Reproduction contract

Run `pixi run study` from the HOOMD experiment directory. Every run stores its
fully resolved TOML configuration and SHA-256 checksum beside the trajectory
and observables. Run `pixi run notebook-execute` afterward to refresh this
notebook from those outputs.
"""
        ),
    ]

    NOTEBOOK.parent.mkdir(parents=True, exist_ok=True)
    nbf.write(notebook, NOTEBOOK)
    print(NOTEBOOK)
    return NOTEBOOK


if __name__ == "__main__":
    build()
