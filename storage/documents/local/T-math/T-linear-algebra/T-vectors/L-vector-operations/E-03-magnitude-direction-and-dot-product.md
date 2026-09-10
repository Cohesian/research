# Magnitude, Direction, and the Dot Product

In Euclidean space, the magnitude of:

$$
\vec v=
\begin{bmatrix}
v_1\\
\vdots\\
v_n
\end{bmatrix}
$$

is:

$$
\lVert\vec v\rVert
=
\sqrt{v_1^2+\cdots+v_n^2}.
$$

It measures how far the vector extends from its local origin.

## Direction through normalization

For $\vec v\neq\vec0$, its normalized direction is:

$$
\widehat{\vec v}
=
\frac{\vec v}{\lVert\vec v\rVert}.
$$

The result has unit magnitude:

$$
\left\lVert\widehat{\vec v}\right\rVert=1.
$$

Therefore:

$$
\vec v
=
\lVert\vec v\rVert\widehat{\vec v}.
$$

This factors the vector into a non-negative magnitude and a unit direction.

## The dot product

For vectors $\vec u,\vec v\in\mathbb{R}^n$:

$$
\vec u\cdot\vec v
=
\sum_{i=1}^{n}u_iv_i.
$$

Geometrically:

$$
\vec u\cdot\vec v
=
\lVert\vec u\rVert
\lVert\vec v\rVert
\cos\theta.
$$

The sign reveals alignment:

- positive: the angle is acute;
- zero: the vectors are orthogonal;
- negative: the angle is obtuse.

For nonzero vectors:

$$
\cos\theta
=
\frac{\vec u\cdot\vec v}
{\lVert\vec u\rVert\lVert\vec v\rVert}.
$$

## Projection

The scalar component of $\vec v$ along $\vec u$ is:

$$
\operatorname{comp}_{\vec u}(\vec v)
=
\frac{\vec v\cdot\vec u}{\lVert\vec u\rVert}.
$$

The vector projection is:

$$
\operatorname{proj}_{\vec u}(\vec v)
=
\frac{\vec v\cdot\vec u}{\vec u\cdot\vec u}\vec u.
$$

Projection converts angular alignment into the amount of one vector carried along another direction.

Magnitude, normalization, angles, and projection rely on an inner-product geometry. They are not consequences of the vector-space axioms alone.
