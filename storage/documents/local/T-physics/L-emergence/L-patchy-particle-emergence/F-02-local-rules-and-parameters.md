# Local Rules and the Controlled Experiment

## Rules executed by the particles

The microscopic model can be summarized without naming a global structure:

1. repel nearby centers through the WCA core;
2. attract nearby, mutually aligned patches with type-dependent strength;
3. sum local force and torque contributions;
4. translate and rotate through Langevin dynamics;
5. exchange energy with the thermal bath; and
6. remain inside the repulsive square barrier.

These rules may permit chains or branches because particles have different
patch counts. They do not demand them.

## Initial state

Particle types are shuffled reproducibly. Orientations are sampled uniformly
from $[-\pi,\pi)$, and momenta are thermalized at the declared $kT$. Initial
positions must respect minimum center distance $1.45$ and the wall margin.

The experiment compares two spatial samplers.

### Random rejection

Candidates are sampled uniformly from the accessible square. A candidate is
accepted when it respects the minimum initial distance. This is unbiased in
position but can produce chance variations in local density.

### Best-candidate blue noise

For every new particle, $96$ uniformly sampled candidates are compared. The
candidate maximizing its distance to the current population is selected,
provided it respects the same minimum distance. This reduces accidental dense
pockets without imposing a lattice.

Blue noise changes only the initial spatial distribution. It is not a force
and does not continue acting after $t=0$.

## Local chemistry

The second experimental axis changes the symmetric attraction matrix
$A_{ab}$.

### Uniform affinity

Every type pair uses

$$
A_{ab}=4.
$$

Patch geometry remains anisotropic, but chemistry does not distinguish types.

### Selective affinity

In type order $(P_1,P_2,P_3)$, the selective matrix is

$$
A=
\begin{pmatrix}
0.20 & 3.50 & 4.00\\
3.50 & 4.00 & 5.00\\
4.00 & 5.00 & 1.50
\end{pmatrix}.
$$

This makes $P_2$--$P_3$ contact strongest, preserves $P_2$--$P_2$ attraction,
and weakens $P_1$--$P_1$ and $P_3$--$P_3$ self-association. The intention is
to permit terminal, chain, and branching roles without specifying one final
graph. The numbers are model parameters, not learned weights or measured
chemical constants.

## The $2\times2$ design

The controlled study is

$$
\mathcal E=
\{\text{random},\text{blue-noise}\}
\times
\{\text{uniform},\text{selective}\}
\times
\{41,137,251\}.
$$

This produces twelve runs. The first two factors define four conditions and
the last factor supplies three independent seeds per condition.

| Quantity | Fixed value |
|---|---:|
| particles $N$ | $96$ |
| type populations $(P_1,P_2,P_3)$ | $(32,48,16)$ |
| square box length | $23$ |
| wall half-width | $10.5$ |
| particle radius | $0.5$ |
| particle mass | $1$ |
| target $kT$ | $0.25$ |
| translational drag | $1.0$ |
| rotational drag | $0.5$ |
| timestep $\Delta t$ | $0.002$ |
| integration steps | $100{,}000$ |
| simulated duration | $200$ |
| save period | $250$ steps $=0.5$ time units |

Density, population, patch geometry, temperature, barriers, timestep,
duration, and observation rules are identical in all twelve runs. Therefore a
difference between chemistry conditions is not simultaneously a difference in
temperature or density.

## Why the earlier two demos are not the control

The earlier baseline and selective demo configurations are visually useful,
but they changed several parameters at once. Comparing their results cannot
attribute a difference to chemistry or initialization. This study replaces
that comparison with a shared base configuration and two explicit axes.

## Experimental identity

Before each run, the study runner materializes a complete resolved TOML file.
Its SHA-256 digest is stored with the run manifest:

$$
\chi_r=\operatorname{SHA256}(\text{resolved configuration}_r).
$$

The checksum identifies the exact numerical input and enables safe result
reuse. It does not prove that the physical model or interpretation is correct.

Generated trajectories remain local because they are large and reproducible.
The tracked scientific resources are the model, study definition, executed
notebook, aggregate tables represented in that notebook, and selected figures.
