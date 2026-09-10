# Reflection as a Linear Transformation

A reflection across a line keeps the component parallel to the mirror and reverses the component perpendicular to it.

Let $\vec u$ be a unit vector along a mirror line through the origin. Every $\vec x\in\mathbb R^2$ decomposes uniquely as:

$$
\vec x=\vec x_{\parallel}+\vec x_{\perp},
$$

where:

$$
\vec x_{\parallel}=(\vec u^{\mathsf T}\vec x)\vec u,
\qquad
\vec x_{\perp}=\vec x-\vec x_{\parallel}.
$$

Reflection changes only the sign of the perpendicular component:

$$
R\vec x=\vec x_{\parallel}-\vec x_{\perp}.
$$

Substituting $\vec x_{\perp}=\vec x-\vec x_{\parallel}$ gives:

$$
R\vec x=2\vec x_{\parallel}-\vec x.
$$

Because $\vec x_{\parallel}=\vec u\vec u^{\mathsf T}\vec x$, the matrix is:

$$
\boxed{R=2\vec u\vec u^{\mathsf T}-I}.
$$

The product $\vec u\vec u^{\mathsf T}$ is the projection matrix onto the mirror line. Reflection can therefore be read as:

$$
\text{twice the projection} - \text{the original vector}.
$$

## What remains unchanged

If $\vec x$ lies on the mirror, then $\vec x_{\perp}=\vec0$ and:

$$
R\vec x=\vec x.
$$

The reflected vector is not zero. What becomes zero is its change under the operator $R-I$:

$$
(R-I)\vec x=\vec0.
$$

If $\vec x$ is perpendicular to the mirror, then $\vec x_{\parallel}=\vec0$ and:

$$
R\vec x=-\vec x.
$$

These two directions will become the two eigendirections of the reflection.

## Reflection is rigid

A reflection preserves lengths and angles:

$$
\|R\vec x\|=\|\vec x\|,
$$

$$
(R\vec x)^{\mathsf T}(R\vec y)=\vec x^{\mathsf T}\vec y.
$$

Equivalently:

$$
R^{\mathsf T}R=I.
$$

It changes orientation but not shape. In two dimensions this is recorded by:

$$
\det(R)=-1.
$$

Applying the same reflection twice returns every vector to its initial position:

$$
R^2=I.
$$
