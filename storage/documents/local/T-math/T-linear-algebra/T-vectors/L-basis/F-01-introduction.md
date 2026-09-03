# Basis: a coordinate language for a vector space

A basis is a set of vectors that is simultaneously sufficient and
nonredundant. It is sufficient because its vectors span the space, and
nonredundant because they are linearly independent.

For a finite-dimensional vector space $V$, a list

$$
\mathcal B=(\mathbf b_1,\ldots,\mathbf b_n)
$$

is a basis when every vector $\mathbf v\in V$ can be written uniquely as

$$
\mathbf v
=v_1\mathbf b_1+\cdots+v_n\mathbf b_n.
$$

The scalars $v_1,\ldots,v_n$ are the coordinates of $\mathbf v$ in
$\mathcal B$:

$$
[\mathbf v]_{\mathcal B}
=
\begin{bmatrix}
v_1\\
\vdots\\
v_n
\end{bmatrix}.
$$

## Span: enough directions

The span of $\mathbf b_1,\ldots,\mathbf b_n$ is

$$
\operatorname{span}\{\mathbf b_1,\ldots,\mathbf b_n\}
=\left\{\sum_{i=1}^{n}\alpha_i\mathbf b_i:
\alpha_i\in\mathbb F\right\}.
$$

If this span equals $V$, the vectors can construct every element of the space.
For example, the standard vectors

$$
\mathbf e_1=
\begin{bmatrix}1\\0\end{bmatrix},
\qquad
\mathbf e_2=
\begin{bmatrix}0\\1\end{bmatrix}
$$

span $\mathbb R^2$ because

$$
\begin{bmatrix}x\\y\end{bmatrix}
=x\mathbf e_1+y\mathbf e_2.
$$

## Linear independence: no redundant direction

The vectors are linearly independent when

$$
\alpha_1\mathbf b_1+\cdots+\alpha_n\mathbf b_n=\mathbf0
$$

implies

$$
\alpha_1=\cdots=\alpha_n=0.
$$

If a nontrivial coefficient choice produces zero, at least one vector can be
constructed from the others. It adds no new direction and coordinates would
not be unique.

For instance,

$$
\begin{bmatrix}1\\0\end{bmatrix},
\begin{bmatrix}0\\1\end{bmatrix},
\begin{bmatrix}1\\1\end{bmatrix}
$$

span $\mathbb R^2$, but they are dependent because the third vector is the
sum of the first two. They form a generating set, not a basis.

## Coordinates depend on the basis

Consider

$$
\mathbf b_1=
\begin{bmatrix}1\\1\end{bmatrix},
\qquad
\mathbf b_2=
\begin{bmatrix}1\\-1\end{bmatrix}.
$$

These vectors form a basis of $\mathbb R^2$. The vector

$$
\mathbf v=
\begin{bmatrix}4\\2\end{bmatrix}
$$

has standard coordinates $(4,2)$, but in $\mathcal B=(\mathbf b_1,\mathbf
b_2)$ it satisfies

$$
\mathbf v=3\mathbf b_1+1\mathbf b_2,
$$

so

$$
[\mathbf v]_{\mathcal B}
=
\begin{bmatrix}3\\1\end{bmatrix}.
$$

The vector did not change. Only its coordinate description changed.

## Change of basis

Let

$$
P_{\mathcal B}
=
\begin{bmatrix}
\vert& &\vert\\
\mathbf b_1&\cdots&\mathbf b_n\\
\vert& &\vert
\end{bmatrix}
$$

contain the new basis vectors as columns in standard coordinates. Then

$$
[\mathbf v]_{\mathrm{std}}
=P_{\mathcal B}[\mathbf v]_{\mathcal B}.
$$

Because a basis is independent, $P_{\mathcal B}$ is invertible, and

$$
[\mathbf v]_{\mathcal B}
=P_{\mathcal B}^{-1}[\mathbf v]_{\mathrm{std}}.
$$

Changing basis is a reversible translation between coordinate languages.

## Dimension, subspaces, and rank

Every basis of a finite-dimensional vector space has the same number of
elements. That number is the dimension:

$$
\dim V=n.
$$

A subspace $U\subseteq V$ has its own basis and dimension. The column space of
a matrix is the span of its columns; its dimension is the matrix rank. Row
reduction exposes pivot columns, which identify a basis for the column space
when traced back to the original matrix.

This gives rank a structural interpretation: it counts the number of
independent output directions preserved by a linear transformation.

## Orthonormal bases

An orthonormal basis satisfies

$$
\mathbf b_i\cdot\mathbf b_j=
\begin{cases}
1,&i=j,\\
0,&i\ne j.
\end{cases}
$$

Coordinates then have the simple projection formula

$$
v_i=\mathbf v\cdot\mathbf b_i.
$$

Orthonormal bases preserve Euclidean length transparently:

$$
\|\mathbf v\|^2=\sum_{i=1}^{n}v_i^2.
$$

A basis is therefore more than a list of axes. It is a local language that
turns abstract vectors and transformations into coordinates while preserving
the underlying linear relations.
