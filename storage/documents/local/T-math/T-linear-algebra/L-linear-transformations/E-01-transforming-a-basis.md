# Transforming a Basis

A transformation $T:V\to W$ is linear when it preserves vector addition and scalar multiplication:

$$
T(\vec u+\vec v)=T(\vec u)+T(\vec v),
$$

$$
T(\alpha\vec v)=\alpha T(\vec v).
$$

Equivalently, it preserves every linear combination:

$$
T(\alpha\vec u+\beta\vec v)
=
\alpha T(\vec u)+\beta T(\vec v).
$$

## A linear map is determined by a basis

Let $(\vec e_1,\ldots,\vec e_n)$ be a basis of $V$. Every vector has a unique expansion:

$$
\vec x=x_1\vec e_1+\cdots+x_n\vec e_n.
$$

Applying linearity:

$$
T(\vec x)
=
x_1T(\vec e_1)+
\cdots+
x_nT(\vec e_n).
$$

Once the images of the basis vectors are known, the image of every vector is forced.

This is the conceptual origin of a matrix.

## Example in two dimensions

Suppose:

$$
T(\vec e_1)=
\begin{bmatrix}2\\1\end{bmatrix},
\qquad
T(\vec e_2)=
\begin{bmatrix}-1\\2\end{bmatrix}.
$$

For:

$$
\vec x=3\vec e_1+4\vec e_2,
$$

linearity gives:

$$
T(\vec x)
=
3
\begin{bmatrix}2\\1\end{bmatrix}
+
4
\begin{bmatrix}-1\\2\end{bmatrix}
=
\begin{bmatrix}2\\11\end{bmatrix}.
$$

The input coordinates $3$ and $4$ have become weights applied to the transformed basis directions.

## What linearity preserves

A linear transformation always maps:

$$
\vec0\longmapsto\vec0.
$$

It also preserves lines through the origin and parallelism. It may rotate, reflect, shear, stretch, contract, or collapse dimensions.

Translations such as:

$$
T(\vec x)=A\vec x+\vec b,
\qquad
\vec b\neq\vec0,
$$

are affine rather than linear because they do not preserve the origin.
