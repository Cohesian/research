# Image, Kernel, and Rank

Let:

$$
A:\mathbb{R}^n\to\mathbb{R}^m.
$$

Two subspaces reveal what the transformation can produce and what it erases.

## Image

The image is the set of all reachable outputs:

$$
\operatorname{im}(A)
=
\{A\vec x\mid\vec x\in\mathbb{R}^n\}.
$$

Because $A\vec x$ is a linear combination of the columns:

$$
\operatorname{im}(A)
=
\operatorname{span}\{\vec a_1,\ldots,\vec a_n\}.
$$

## Kernel

The kernel contains every input mapped to zero:

$$
\ker(A)
=
\{\vec x\in\mathbb{R}^n\mid A\vec x=\vec0\}.
$$

If the kernel contains a nonzero vector, at least one input direction has been collapsed.

## Rank and nullity

The rank is the dimension of the image:

$$
\operatorname{rank}(A)=\dim\operatorname{im}(A).
$$

The nullity is the dimension of the kernel:

$$
\operatorname{nullity}(A)=\dim\ker(A).
$$

For a linear map with an $n$-dimensional domain:

$$
\operatorname{rank}(A)+\operatorname{nullity}(A)=n.
$$

This is the rank–nullity theorem.

## Dependence between columns

If one column is a linear combination of the others, it adds no new direction to the image. The matrix may have many columns while having a smaller rank.

For example:

$$
A=
\begin{bmatrix}
1&2\\
2&4
\end{bmatrix}
$$

has two columns, but the second is twice the first. Therefore:

$$
\operatorname{rank}(A)=1.
$$

The plane is collapsed onto a line.

For a square $n\times n$ matrix, invertibility is equivalent to full rank, a trivial kernel, and linearly independent columns.
