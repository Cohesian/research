# From Trajectories to Macroscopic Observables

## A declared projection

HOOMD evolves continuous positions and orientations. It does not create
persistent graph bonds. Research therefore declares an analysis projection
for each saved frame:

$$
X(t)\xrightarrow{\Pi_G}G_t=(V,E_t)
\xrightarrow{\Pi_M}M(t).
$$

The contact graph is a measurement of the trajectory, not an additional force
in the simulation.

## Contact rule

For pair $i,j$, define

$$
\mathbf r_{ij}=\mathbf x_j-\mathbf x_i,
\qquad
r_{ij}=\|\mathbf r_{ij}\|,
\qquad
\widehat{\mathbf r}_{ij}=\frac{\mathbf r_{ij}}{r_{ij}}.
$$

Let $\mathcal D_i(t)$ be particle $i$'s patch directors rotated into the world
frame. The best mutual alignments are

$$
a_i^{(ij)}=
\max_{\mathbf d\in\mathcal D_i(t)}
\mathbf d\cdot\widehat{\mathbf r}_{ij},
$$

and

$$
a_j^{(ji)}=
\max_{\mathbf d\in\mathcal D_j(t)}
\mathbf d\cdot\left(-\widehat{\mathbf r}_{ij}\right).
$$

An undirected contact edge is present when

$$
\{i,j\}\in E_t
\iff
r_{ij}\le1.45
\quad\land\quad
a_i^{(ij)}\ge0.93
\quad\land\quad
a_j^{(ji)}\ge0.93.
$$

The thresholds are analysis parameters. Changing them changes the graph
projection and must be treated as a different measurement definition.

## Largest connected fraction

Let $\operatorname{CC}(G_t)$ be the set of connected components. Define

$$
S_{\max}(t)=
\frac{1}{N}
\max_{C\in\operatorname{CC}(G_t)}|C|.
$$

This quantity is $1/N$ when every particle is isolated and $1$ when the
contact graph is connected. The run maximum detects a transient large
structure. The tail mean tests whether connectivity remains elevated late in
the run.

## Mean contact degree

The mean degree is

$$
\langle k\rangle_t
=\frac1N\sum_i k_i(t)
=\frac{2|E_t|}{N}.
$$

Two systems can have the same largest component but different mean degree. A
linear chain, a branched tree, and a cyclic cluster differ topologically even
when they contain the same number of particles.

## Orientational order

For planar orientation $\theta_i(t)$, the order-$m$ parameter is

$$
\Psi_m(t)=
\left|
\frac1N\sum_{i=1}^{N}e^{\mathrm i m\theta_i(t)}
\right|.
$$

The study uses $m=2$. Values near zero indicate cancellation across the
population; larger values indicate shared twofold alignment. This global
statistic is independent of whether aligned particles are connected by the
contact rule.

## Energy and kinetic temperature

The total kinetic energy contains translation and rotation:

$$
K(t)=
\sum_i\frac12m_i\|\mathbf v_i\|^2
+\sum_i\frac12I_i\omega_i^2.
$$

Potential energy $U(t)$ is computed from the pair and wall potentials. The
kinetic temperature checks whether the Langevin thermostat samples near its
target. Since the heat bath exchanges energy with the system, $U+K$ need not
remain constant.

## Temporal summaries

For each run, Research records:

- maximum $S_{\max}$ and the time at which it occurs;
- the mean of $S_{\max}$ over the final $25\%$ of saved frames;
- tail mean degree, orientational order, kinetic temperature, $U$, and $K$;
- the fraction of frames satisfying $S_{\max}\ge0.10$.

The last quantity is a declared persistence statistic:

$$
P_{0.10}^{(r)}=
\frac1{T_r}
\sum_{n=1}^{T_r}
\mathbf1\!\left[S_{\max}^{(r)}(t_n)\ge0.10\right].
$$

It does not mean that a particular component survives continuously; component
identity is not tracked in this first study.

## Ensemble summaries

For scalar run summary $A_r$ across $R=3$ seeds, the condition mean is

$$
\overline A=\frac1R\sum_{r=1}^{R}A_r,
$$

and the displayed sample standard deviation is

$$
s_A=
\sqrt{
\frac{1}{R-1}
\sum_{r=1}^{R}(A_r-\overline A)^2
}.
$$

Individual seed points remain visible in the report. With only three seeds,
the error bars describe the observed sample and should not be read as narrow
confidence intervals.

## When a projection becomes an effective law

A macroscopic observable is not automatically a law. A stronger claim would
require its distribution to become reproducible across seeds and system sizes,
and ideally an approximately closed evolution

$$
M(t+\Delta t)\approx\Phi\bigl(M(t)\bigr)
$$

whose error is quantified in a declared regime. This experiment stops earlier:
it measures whether one controlled local-rule change produces a detectable
macroscopic difference.
