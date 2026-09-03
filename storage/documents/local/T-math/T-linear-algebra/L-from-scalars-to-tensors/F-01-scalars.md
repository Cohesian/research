# Scalars: magnitude, scale, and the coefficient system

Linear algebra separates the objects being transformed from the numbers used
to combine them. Those numbers are **scalars**.

Most elementary examples use the real numbers $\mathbb{R}$, while systems
involving phase, oscillation, or quantum amplitudes often use the complex
numbers $\mathbb{C}$. The chosen scalar system is called the field over which
a vector space is defined.

## Scalars as quantities

A scalar has magnitude but no intrinsic spatial direction. Examples include

$$
3,\qquad -\frac12,\qquad \pi,\qquad 2+3i.
$$

Applications may attach units to a scalar: five seconds, twelve kilograms, or
twenty degrees. The numerical scalar and its physical interpretation should
not be confused. Algebra manipulates the coefficient; dimensional analysis
checks whether the surrounding quantities are compatible.

## Scalars as transformations

Multiplying a vector $\mathbf v$ by a scalar $\alpha$ changes its scale:

$$
\mathbf v\longmapsto \alpha\mathbf v.
$$

Over a real vector space:

- $|\alpha|>1$ stretches the vector;
- $0<|\alpha|<1$ contracts it;
- $\alpha=0$ collapses it to the zero vector;
- $\alpha<0$ also reverses its orientation.

Thus a scalar is not only a stored magnitude. Through multiplication it acts
as a simple linear transformation.

## Why a field is useful

A scalar field supports addition, subtraction, multiplication, and division
by nonzero elements while remaining inside the same system. In particular,
every nonzero scalar $\alpha$ has an inverse $\alpha^{-1}$ such that

$$
\alpha\alpha^{-1}=1.
$$

This permits equations such as

$$
\alpha\mathbf x=\mathbf v
$$

to be solved by

$$
\mathbf x=\alpha^{-1}\mathbf v=\frac{1}{\alpha}\mathbf v.
$$

Division of a vector is therefore scalar multiplication by an inverse; there
is no independent vector-division operation here.

## One-dimensional coordinates

Choose a nonzero basis vector $\mathbf e$. Every vector in its one-dimensional
span has the form

$$
\mathbf v=x\mathbf e.
$$

The vector $\mathbf v$ is the geometric or abstract object. The scalar $x$ is
its coordinate relative to the chosen basis.

Changing the basis changes the coordinate without changing the vector. If

$$
\mathbf e'=2\mathbf e,
$$

then

$$
6\mathbf e=3\mathbf e'.
$$

The same vector is represented by coordinate $6$ in one basis and $3$ in the
other. Coordinates are therefore descriptions, not the underlying object.

## Scalar combinations

Given vectors $\mathbf v_1,\ldots,\mathbf v_n$ and scalars
$\alpha_1,\ldots,\alpha_n$, an expression of the form

$$
\alpha_1\mathbf v_1+\cdots+\alpha_n\mathbf v_n
$$

is a linear combination. Scalars determine how much of each vector
participates. The sets of all such combinations lead to span, basis,
subspaces, and ultimately coordinates in multiple dimensions.

