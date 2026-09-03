# Reflection: symmetry through projection

A reflection preserves lengths and angles while reversing one component of a
vector. Its cleanest formulas arise by decomposing a vector into parts parallel
and perpendicular to the reflecting subspace.

## Reflection across a hyperplane through the origin

Let $\widehat{\mathbf n}$ be a unit normal vector to a hyperplane. Every vector
$\mathbf v$ decomposes as

$$
\mathbf v
=\mathbf v_{\parallel}+\mathbf v_{\perp},
$$

where

$$
\mathbf v_{\perp}
=(\mathbf v\cdot\widehat{\mathbf n})\widehat{\mathbf n}
$$

and

$$
\mathbf v_{\parallel}
=\mathbf v-\mathbf v_{\perp}.
$$

Reflection keeps the parallel component and negates the perpendicular one:

$$
R(\mathbf v)
=\mathbf v_{\parallel}-\mathbf v_{\perp}.
$$

Substituting the decomposition yields

$$
R(\mathbf v)
=\mathbf v-2(\mathbf v\cdot\widehat{\mathbf n})
\widehat{\mathbf n}.
$$

The factor two appears because the perpendicular component is first removed
and then added in the opposite direction.

## Example: reflection across the $x$-axis

The $x$-axis has unit normal

$$
\widehat{\mathbf n}=
\begin{bmatrix}0\\1\end{bmatrix}.
$$

For

$$
\mathbf v=
\begin{bmatrix}3\\4\end{bmatrix},
$$

the perpendicular component is

$$
(\mathbf v\cdot\widehat{\mathbf n})\widehat{\mathbf n}
=4
\begin{bmatrix}0\\1\end{bmatrix}
=
\begin{bmatrix}0\\4\end{bmatrix}.
$$

Therefore

$$
R(\mathbf v)
=
\begin{bmatrix}3\\4\end{bmatrix}
-2
\begin{bmatrix}0\\4\end{bmatrix}
=
\begin{bmatrix}3\\-4\end{bmatrix}.
$$

## Reflection across a line

In two dimensions, let $\widehat{\mathbf u}$ be a unit direction along the
reflecting line. Keep the projection onto the line and reverse the remaining
component:

$$
R(\mathbf v)
=2(\mathbf v\cdot\widehat{\mathbf u})
\widehat{\mathbf u}-\mathbf v.
$$

This formula and the normal-vector formula describe the same geometry from
complementary perspectives.

## Householder matrix

The hyperplane reflection can be written as a matrix

$$
H=I-2\widehat{\mathbf n}\widehat{\mathbf n}^{\mathsf T}.
$$

Then

$$
R(\mathbf v)=H\mathbf v.
$$

The outer product

$$
\widehat{\mathbf n}\widehat{\mathbf n}^{\mathsf T}
$$

is the matrix of orthogonal projection onto the normal direction. The
Householder matrix subtracts twice that projection.

It satisfies

$$
H^{\mathsf T}=H,
\qquad
H^{\mathsf T}H=I,
\qquad
H^2=I.
$$

These equations say that the reflection is symmetric, preserves inner
products, and is its own inverse. Reflecting twice restores the original
vector.

The determinant is $-1$: magnitude one because volume is preserved, negative
because orientation is reversed.

## Reflection across an affine hyperplane

If the reflecting hyperplane passes through a point $\mathbf p$ rather than the
origin, translate to local coordinates, reflect, and translate back:

$$
R_{\mathbf p}(\mathbf x)
=\mathbf p
+H(\mathbf x-\mathbf p).
$$

This map is affine. Its internal reflection $H$ is linear, while the offset
$\mathbf p$ moves the fixed hyperplane away from the origin.

## Reflection as a reusable pattern

Reflection illustrates a general linear-algebra strategy:

1. identify a meaningful subspace;
2. project the input into complementary components;
3. transform each component with a simple scalar rule;
4. recombine the result.

The geometry looks global, but the construction is local to two orthogonal
components: one remains invariant and the other changes sign.
