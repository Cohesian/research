# Coordinates and Basis

A basis is an ordered collection of vectors that is both linearly independent and spanning.

Let:

$$
\mathcal B=(\vec b_1,\ldots,\vec b_n)
$$

be a basis of an $n$-dimensional vector space $V$. Every $\vec v\in V$ can be written uniquely as:

$$
\vec v
=
x_1\vec b_1+\cdots+x_n\vec b_n.
$$

The coefficients form its coordinate column:

$$
[\vec v]_{\mathcal B}
=
\begin{bmatrix}
x_1\\
\vdots\\
x_n
\end{bmatrix}.
$$

## The standard basis

In $\mathbb{R}^3$, the standard basis is:

$$
\vec e_1=
\begin{bmatrix}1\\0\\0\end{bmatrix},
\qquad
\vec e_2=
\begin{bmatrix}0\\1\\0\end{bmatrix},
\qquad
\vec e_3=
\begin{bmatrix}0\\0\\1\end{bmatrix}.
$$

Thus:

$$
\vec v=
\begin{bmatrix}x\\y\\z\end{bmatrix}
=
x\vec e_1+y\vec e_2+z\vec e_3.
$$

The coordinates $x,y,z$ are scalar instructions telling how much of each basis direction contributes to the vector.

## A basis need not be orthonormal

Basis vectors do not need to have unit length, and they do not need to be perpendicular. They only need to be independent and span the space.

For example:

$$
\vec b_1=
\begin{bmatrix}1\\0\end{bmatrix},
\qquad
\vec b_2=
\begin{bmatrix}1\\1\end{bmatrix}
$$

form a basis of $\mathbb{R}^2$ even though they are not orthogonal.

The vector:

$$
\vec v=
\begin{bmatrix}3\\2\end{bmatrix}
$$

has standard coordinates $(3,2)$, but relative to $\mathcal B=(\vec b_1,\vec b_2)$:

$$
\vec v=1\vec b_1+2\vec b_2,
$$

so:

$$
[\vec v]_{\mathcal B}
=
\begin{bmatrix}1\\2\end{bmatrix}.
$$

## Coordinates are descriptions

Changing basis changes the coordinate list, not the underlying vector.

If the basis vectors are placed as columns of a matrix:

$$
B=
\begin{bmatrix}
|&|&&|\\
\vec b_1&\vec b_2&\cdots&\vec b_n\\
|&|&&|
\end{bmatrix},
$$

then coordinates reconstruct the vector through:

$$
\vec v=B[\vec v]_{\mathcal B}.
$$

When $B$ is invertible:

$$
[\vec v]_{\mathcal B}=B^{-1}\vec v.
$$

This matrix equation is the bridge from basis coordinates to linear transformations.
