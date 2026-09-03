# Linear transformations and their matrix representations

A linear transformation is a function between vector spaces that preserves
their two defining operations. A map

$$
T:V\to W
$$

is linear when, for all vectors $\mathbf u,\mathbf v\in V$ and scalars
$\alpha$,

$$
T(\mathbf u+\mathbf v)=T(\mathbf u)+T(\mathbf v)
$$

and

$$
T(\alpha\mathbf v)=\alpha T(\mathbf v).
$$

Equivalently, it preserves every linear combination:

$$
T(\alpha\mathbf u+\beta\mathbf v)
=\alpha T(\mathbf u)+\beta T(\mathbf v).
$$

## A transformation is determined by a basis

Let $\mathbf e_1,\ldots,\mathbf e_n$ be a basis of $V$. Every vector has a
unique expansion

$$
\mathbf v=v_1\mathbf e_1+\cdots+v_n\mathbf e_n.
$$

Linearity forces

$$
T(\mathbf v)
=v_1T(\mathbf e_1)+\cdots+v_nT(\mathbf e_n).
$$

Therefore, knowing the images of the basis vectors determines the image of
every vector.

## Matrices store those images

After choosing bases for $V$ and $W$, place the coordinate vectors of
$T(\mathbf e_i)$ into the columns of a matrix $A$:

$$
A=
\begin{bmatrix}
\vert & & \vert\\
[T(\mathbf e_1)] & \cdots & [T(\mathbf e_n)]\\
\vert & & \vert
\end{bmatrix}.
$$

Then

$$
[T(\mathbf v)]=A[\mathbf v].
$$

For example, let

$$
A=
\begin{bmatrix}
2&1\\
0&1
\end{bmatrix}.
$$

Its columns say

$$
T(\mathbf e_1)=
\begin{bmatrix}2\\0\end{bmatrix},
\qquad
T(\mathbf e_2)=
\begin{bmatrix}1\\1\end{bmatrix}.
$$

For

$$
\mathbf v=
\begin{bmatrix}3\\4\end{bmatrix}
=3\mathbf e_1+4\mathbf e_2,
$$

we obtain

$$
A\mathbf v
=3
\begin{bmatrix}2\\0\end{bmatrix}
+4
\begin{bmatrix}1\\1\end{bmatrix}
=
\begin{bmatrix}10\\4\end{bmatrix}.
$$

Matrix-vector multiplication is thus a weighted combination of the matrix's
columns.

## The map and the matrix are not identical concepts

The abstract transformation $T$ exists independently of coordinates. Its
matrix changes when the domain or codomain basis changes. A matrix is a
representation of a linear map relative to selected bases.

This is the same distinction seen between a vector and its coordinate tuple.
Coordinates make computation concrete, but they introduce a perspective.

## Composition becomes multiplication

If

$$
T:V\to W
\qquad\text{and}\qquad
S:W\to U,
$$

then the composition $S\circ T$ is linear. With compatible bases, if $A$
represents $T$ and $B$ represents $S$, then

$$
[S(T(\mathbf v))]=BA[\mathbf v].
$$

The rightmost transformation acts first. Matrix multiplication encodes the
composition of transformations.

## Structure exposed by a matrix

Several matrix concepts describe the transformation itself:

- the **kernel** contains inputs sent to zero;
- the **image** contains attainable outputs;
- the **rank** is the dimension of the image;
- for a square matrix, a nonzero determinant means the map is invertible;
- the absolute determinant measures oriented volume scaling.

The rank-nullity theorem connects lost and preserved directions:

$$
\dim V=\dim(\ker T)+\dim(\operatorname{im}T).
$$

## Linear versus affine motion

Every linear map sends zero to zero:

$$
T(\mathbf0)=\mathbf0.
$$

A translation

$$
\mathbf v\mapsto A\mathbf v+\mathbf b,
\qquad \mathbf b\ne\mathbf0,
$$

does not satisfy this condition and is therefore affine rather than linear.
Rotations, reflections through the origin, projections onto subspaces, and
scalings are linear; arbitrary shifts require the additional offset.

