# Scalar Multiplication

Let $\vec v$ be a vector and let $\alpha$ be a scalar. Scalar multiplication produces:

$$
\alpha\vec v.
$$

In coordinates:

$$
\alpha
\begin{bmatrix}
v_1\\
\vdots\\
v_n
\end{bmatrix}
=
\begin{bmatrix}
\alpha v_1\\
\vdots\\
\alpha v_n
\end{bmatrix}.
$$

Every coordinate is scaled by the same factor, so the vector remains on the same one-dimensional subspace:

$$
\operatorname{span}\{\vec v\}.
$$

## Geometric cases

For a nonzero Euclidean vector:

- $\alpha>1$ stretches it without changing direction;
- $0<\alpha<1$ contracts it without changing direction;
- $\alpha=0$ returns $\vec0$;
- $\alpha<0$ reverses direction and scales by $|\alpha|$.

The norm follows:

$$
\lVert\alpha\vec v\rVert
=
|\alpha|\lVert\vec v\rVert.
$$

## Division by a scalar

For $\alpha\neq0$:

$$
\frac{\vec v}{\alpha}
=
\frac{1}{\alpha}\vec v.
$$

Vector division here is only shorthand for reciprocal scalar multiplication. It does not define division by another vector.

## Linear interpolation

The points on the line through position vectors $\vec a$ and $\vec b$ can be written as:

$$
\vec p(t)
=(1-t)\vec a+t\vec b
=
\vec a+t(\vec b-\vec a).
$$

For $0\leq t\leq1$, this traces the segment from $A$ to $B$:

$$
\vec p(0)=\vec a,
\qquad
\vec p(1)=\vec b.
$$

At $t=1/2$ it returns the midpoint.

This construction is another example of scalars controlling position through a linear combination.
