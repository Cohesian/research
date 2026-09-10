# Eigendirections and Invariants

A nonzero vector $\vec v$ is an eigenvector of a linear transformation $R$ when:

$$
R\vec v=\lambda\vec v.
$$

Reflection exposes this definition geometrically.

## The mirror direction

Every vector parallel to the mirror is fixed:

$$
R\vec u=\vec u.
$$

Thus the mirror line is the eigenspace for eigenvalue $+1$:

$$
E_{+1}
=
\ker(R-I).
$$

This kernel notation formalizes the observation that $(R-I)\vec u=\vec0$.

## The normal direction

Every vector perpendicular to the mirror reverses direction:

$$
R\vec n=-\vec n.
$$

Therefore the normal line is the eigenspace for eigenvalue $-1$:

$$
E_{-1}
=
\ker(R+I).
$$

Reflection does not collapse either direction. Both eigenvalues have absolute value one, so lengths are preserved.

## Every vector is assembled from both eigenspaces

Because $\vec u$ and $\vec n$ form a basis of $\mathbb R^2$, every vector can be written as:

$$
\vec x=\alpha\vec u+\beta\vec n.
$$

Then:

$$
R\vec x
=
\alpha R\vec u+\beta R\vec n
=
\alpha\vec u-\beta\vec n.
$$

The matrix operation is therefore a coordinate sign change in its eigenbasis.

## Invariants that identify a planar reflection

For a reflection through a line in $\mathbb R^2$:

$$
R^{\mathsf T}R=I,
\qquad
R^2=I,
\qquad
\det(R)=-1,
\qquad
\operatorname{tr}(R)=0.
$$

Its spectrum is:

$$
\sigma(R)=\{+1,-1\}.
$$

The eigenvector with eigenvalue $+1$ reveals the mirror. The eigenvector with eigenvalue $-1$ reveals its normal.

## Higher-dimensional reflection

In $\mathbb R^n$, a reflection across the hyperplane perpendicular to a unit normal $\vec n$ is:

$$
H=I-2\vec n\vec n^{\mathsf T}.
$$

This is a Householder reflection. Every vector in the hyperplane has eigenvalue $+1$, while the normal direction has eigenvalue $-1$.

The same local rule scales to any finite dimension: preserve the tangent subspace, reverse the normal component.
