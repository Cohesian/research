# Constructing a Reflection Matrix

## From any direction vector

The mirror direction does not need to arrive normalized. For a nonzero vector $\vec a$, its unit direction is:

$$
\vec u=\frac{\vec a}{\|\vec a\|}.
$$

The projection onto $\operatorname{span}\{\vec a\}$ is:

$$
P
=
\vec u\vec u^{\mathsf T}
=
\frac{\vec a\vec a^{\mathsf T}}{\vec a^{\mathsf T}\vec a}.
$$

Therefore:

$$
\boxed{
R
=
2P-I
=
2\frac{\vec a\vec a^{\mathsf T}}{\vec a^{\mathsf T}\vec a}-I
}.
$$

Normalization is not cosmetic. Without the denominator $\vec a^{\mathsf T}\vec a$, the outer product would also scale the result.

## A mirror at angle $\theta$

Let the mirror make angle $\theta$ with the positive horizontal axis:

$$
\vec u=
\begin{bmatrix}
\cos\theta\\
\sin\theta
\end{bmatrix}.
$$

Substituting it into $R=2\vec u\vec u^{\mathsf T}-I$ gives:

$$
R_{\theta}
=
\begin{bmatrix}
\cos(2\theta)&\sin(2\theta)\\
\sin(2\theta)&-\cos(2\theta)
\end{bmatrix}.
$$

The doubled angle appears because a reflected direction crosses the mirror by the same angular distance on the opposite side.

Some familiar cases are:

$$
R_0=
\begin{bmatrix}
1&0\\
0&-1
\end{bmatrix}
\qquad
\text{(horizontal mirror)},
$$

$$
R_{\pi/4}=
\begin{bmatrix}
0&1\\
1&0
\end{bmatrix}
\qquad
\text{(mirror }y=x\text{)}.
$$

The second matrix swaps the two coordinates.

## The eigenbasis construction

Let $\vec n$ be a unit normal to the mirror. The orthogonal matrix:

$$
Q=
\begin{bmatrix}
|&|\\
\vec u&\vec n\\
|&|
\end{bmatrix}
$$

changes from mirror-aligned coordinates to standard coordinates. In the mirror-aligned basis, reflection is simply:

$$
D=
\begin{bmatrix}
1&0\\
0&-1
\end{bmatrix}.
$$

Returning to standard coordinates yields:

$$
\boxed{R=QDQ^{\mathsf T}}.
$$

This says exactly what the geometry says: retain the mirror coordinate and negate the normal coordinate.

## Mirrors away from the origin

A linear reflection must preserve the origin. If the mirror passes through a point $\vec p\neq\vec0$, first move the point into mirror-centered coordinates, reflect, and move it back:

$$
\mathcal R(\vec x)
=
\vec p+R(\vec x-\vec p).
$$

This is an affine reflection rather than a linear transformation.
