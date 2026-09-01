# The Patchy-Particle Model

## Reduced units and geometry

The experiment uses dimensionless reduced units. Length, mass, energy, and time
are internally consistent, but they are not mapped to meters, kilograms,
joules, or seconds. The system is a two-dimensional square bounded by four
repulsive planes.

Every particle has disk radius $R=0.5$, diameter $\sigma=1$, and mass $m=1$.
The moment of inertia around its local $z$ axis is that of a uniform disk:

$$
I=\frac12mR^2=0.125.
$$

## Types and patches

There are three particle types:

| Type | Patch count | Population | Geometric role made possible |
|---|---:|---:|---|
| $P_1$ | $1$ | $32$ | terminal contact |
| $P_2$ | $2$ | $48$ | chain-like continuation |
| $P_3$ | $3$ | $16$ | branching contact |

The final column is a geometric capacity, not a prescribed behavior. A
three-patch particle is not told to become a branch point.

For a type with $p$ patches, the body-fixed patch directors are evenly spaced:

$$
\mathbf d_k^{(p)}=
\left(
\cos\frac{2\pi k}{p},
\sin\frac{2\pi k}{p},
0
\right),
\qquad
k=0,\ldots,p-1.
$$

The particle orientation rotates these directors into the world frame.

## Microscopic state

Particle $i$ has static type $\tau_i\in\{P_1,P_2,P_3\}$ and dynamic state

$$
s_i(t)=
\bigl(
\mathbf x_i(t),
\mathbf v_i(t),
q_i(t),
\mathbf L_i(t)
\bigr),
$$

where $\mathbf x_i$ is position, $\mathbf v_i$ is velocity, $q_i$ is the
orientation quaternion, and $\mathbf L_i$ is angular momentum. Motion is
restricted to the $xy$ plane, while HOOMD stores orientation in its standard
quaternion representation.

## Total potential energy

For configuration $X$, the conservative potential is

$$
U(X)=
\sum_{i<j}
\left[
U_{\mathrm{WCA}}(r_{ij})
+U_{\mathrm{patch}}(r_{ij},q_i,q_j)
\right]
+\sum_iU_{\mathrm{wall}}(\mathbf x_i).
$$

The three terms provide short-range exclusion, directional attraction, and
containment.

## Repulsive core

The isotropic pair core is the shifted Lennard--Jones potential truncated at
its minimum:

$$
U_{\mathrm{WCA}}(r)=
\begin{cases}
4\epsilon_r
\left[
\left(\dfrac{\sigma}{r}\right)^{12}
-\left(\dfrac{\sigma}{r}\right)^6
\right]+epsilon_r,
& r<2^{1/6}\sigma,\\[8pt]
0,&r\ge 2^{1/6}\sigma.
\end{cases}
$$

Here $\epsilon_r=1$. The same repulsive form acts between each particle and
the four walls. This is a soft but steep excluded-volume energy, not a literal
Pauli-exclusion model.

## Directional patch attraction

For particles $i$ and $j$, HOOMD's patch potential sums over every pair of
their patch directors:

$$
U_{ij}^{\mathrm{patch}}=
\sum_{a\in\mathcal D_i}
\sum_{b\in\mathcal D_j}
f(\theta_{a,i};\alpha,\omega)
f(\theta_{b,j};\alpha,\omega)
U_{\mathrm G}^{\mathrm{shift}}(r_{ij}).
$$

Before cutoff shifting, the radial term is

$$
U_{\mathrm G}(r)=
-A_{\tau_i\tau_j}
\exp\left[
-\frac12\left(\frac{r}{\sigma_p}\right)^2
\right],
$$

where $A_{\tau_i\tau_j}=A_{\tau_j\tau_i}\ge0$ is the attraction magnitude and
$\sigma_p=1$ is its radial range. The interaction is truncated and shifted to
zero at $r_c=1.8$.

The angular envelope is a normalized logistic function. Define

$$
h(\theta)=
\left[
1+\exp\bigl(-\omega(\cos\theta-\cos\alpha)\bigr)
\right]^{-1}.
$$

Then

$$
f(\theta;\alpha,\omega)
=\frac{h(\theta)-h(\pi)}{h(0)-h(\pi)}.
$$

The model uses half-angle $\alpha=0.30$ radians and steepness $\omega=45$.
Consequently, a patch contributes strongly only when its director points close
to the center-to-center direction. Because the potential depends on both
position and orientation, it produces force and torque:

$$
\mathbf F_i^{\mathrm C}=-\nabla_{\mathbf x_i}U,
\qquad
\boldsymbol\tau_i^{\mathrm C}
=-\frac{\partial U}{\partial q_i}
\quad\text{in HOOMD's rotational representation}.
$$

The attractive Gaussian has no rest length. Its preference for close contact
is balanced by the WCA core.

## Langevin dynamics

The translational degrees of freedom follow

$$
m\frac{d\mathbf v_i}{dt}
=\mathbf F_i^{\mathrm C}
-\gamma\mathbf v_i
+\mathbf F_i^{\mathrm R},
\qquad
\frac{d\mathbf x_i}{dt}=\mathbf v_i.
$$

The random force has zero mean, and in $d$ spatial dimensions HOOMD chooses its
variance consistently with the timestep and heat bath:

$$
\left\langle\mathbf F_i^{\mathrm R}\right\rangle=0,
\qquad
\left\langle|\mathbf F_i^{\mathrm R}|^2\right\rangle
=\frac{2d\,kT\gamma}{\Delta t}.
$$

Rotation has the analogous form

$$
I\frac{d\boldsymbol\omega_i}{dt}
=\boldsymbol\tau_i^{\mathrm C}
-\gamma_r\boldsymbol\omega_i
+\boldsymbol\tau_i^{\mathrm R}.
$$

This experiment uses $kT=0.25$, translational drag $\gamma=1$, rotational drag
$\gamma_r=0.5$, and timestep $\Delta t=0.002$. Force changes momentum; the
evolving velocity changes position. Multiplying force directly by $\Delta t$
would not be the model.

The Langevin bath makes the dynamics stochastic and open. Mechanical energy
$U+K$ is therefore not conserved: drag and random forcing exchange energy with
the reservoir.

## Local computation and synchronized time

Pair forces vanish beyond their cutoffs, so a cell neighbor list can compute
them from finite spatial neighborhoods. HOOMD advances all positions,
velocities, orientations, and angular momenta on a shared numerical clock. The
simulation is locally interacting but synchronously integrated.

## Implementation references

- [HOOMD Patchy potential](https://hoomd-blue.readthedocs.io/en/stable/hoomd/md/pair/aniso/patchy.html)
- [HOOMD PatchyGaussian](https://hoomd-blue.readthedocs.io/en/stable/hoomd/md/pair/aniso/patchygaussian.html)
- [HOOMD Langevin method](https://hoomd-blue.readthedocs.io/en/stable/hoomd/md/methods/langevin.html)
- [HOOMD GSD trajectory writer](https://hoomd-blue.readthedocs.io/en/stable/hoomd/write/gsd.html)
