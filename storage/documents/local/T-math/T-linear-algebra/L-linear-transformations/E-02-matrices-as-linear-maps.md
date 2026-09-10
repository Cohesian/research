# Matrices as Linear Maps

Choose a basis for an $n$-dimensional input space and a basis for an $m$-dimensional output space. A linear transformation:

$$
T:\mathbb{R}^n\to\mathbb{R}^m
$$

is represented by an $m\times n$ matrix:

$$
A=
\begin{bmatrix}
|&|&&|\\
\vec a_1&\vec a_2&\cdots&\vec a_n\\
|&|&&|
\end{bmatrix}.
$$

Each column $\vec a_j\in\mathbb{R}^m$ is the image of one input basis vector:

$$
\vec a_j=A\vec e_j.
$$

## Why the dimensions have this shape

The input vector has $n$ coordinates:

$$
\vec x\in\mathbb{R}^n.
$$

Therefore the matrix needs $n$ columns—one transformed basis vector for each input coordinate.

Every column lies in the output space $\mathbb{R}^m$, so each column needs $m$ entries. Thus:

$$
A\in\mathbb{R}^{m\times n},
\qquad
A\vec x\in\mathbb{R}^m.
$$

## Rectangularity is structural

A matrix cannot have ragged columns of different lengths. All columns represent vectors in the same codomain and therefore share the same dimension.

An entry written as zero is meaningful:

$$
0
$$

says that a particular output coordinate receives no contribution from that matrix coefficient. A blank entry is not automatically zero unless the representation protocol explicitly defines it that way.

## Dense and sparse matrices

A dense matrix stores or conceptually includes many nonzero entries. A sparse matrix contains mostly zeros and may use a compressed storage format.

Density does not change the mathematical shape:

$$
m\times n.
$$

It changes how efficiently the matrix may be represented and computed.

## Square matrices

When $m=n$, the transformation maps a space back into one of the same dimension:

$$
T:\mathbb{R}^n\to\mathbb{R}^n.
$$

This does not guarantee invertibility. A square matrix may still collapse independent directions into a lower-dimensional image.
