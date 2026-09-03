# A simple tensor: multilinear structure beyond matrices

The word **tensor** is used at several levels. In numerical software it often
means a multidimensional array. In linear algebra, a tensor is an object whose
meaning is independent of coordinates and whose coordinate entries transform
consistently when bases change.

A useful first step is the tensor product of two vectors.

## From pairs to a bilinear product

Let $\mathbf u\in V$ and $\mathbf v\in W$. Their tensor product is written

$$
\mathbf u\otimes\mathbf v\in V\otimes W.
$$

It is linear in each input separately:

$$
(\alpha\mathbf u_1+\beta\mathbf u_2)\otimes\mathbf v
=\alpha(\mathbf u_1\otimes\mathbf v)
+\beta(\mathbf u_2\otimes\mathbf v),
$$

and similarly in the second input.

A tensor that can be written as one product $\mathbf u\otimes\mathbf v$ is
called **simple**, **elementary**, or **decomposable**. General tensors are
finite sums of simple tensors.

## Coordinate representation as an outer product

Given coordinate vectors

$$
\mathbf u=
\begin{bmatrix}1\\2\end{bmatrix},
\qquad
\mathbf v=
\begin{bmatrix}3\\4\\5\end{bmatrix},
$$

the simple tensor has the array representation

$$
\mathbf u\mathbf v^{\mathsf T}
=
\begin{bmatrix}
1\\2
\end{bmatrix}
\begin{bmatrix}
3&4&5
\end{bmatrix}
=
\begin{bmatrix}
3&4&5\\
6&8&10
\end{bmatrix}.
$$

Every column is a scalar multiple of $\mathbf u$, and every row is a scalar
multiple of $\mathbf v^{\mathsf T}$. The matrix therefore has rank one. This
factorized structure is the coordinate signature of a nonzero simple tensor
of two vectors.

Not every matrix is one outer product. For example, the identity matrix

$$
I=
\begin{bmatrix}1&0\\0&1\end{bmatrix}
$$

has rank two and must be expressed as a sum of at least two rank-one outer
products:

$$
I=\mathbf e_1\mathbf e_1^{\mathsf T}
+\mathbf e_2\mathbf e_2^{\mathsf T}.
$$

## Vectors, covectors, and bilinear forms

A covector is a linear map from vectors to scalars:

$$
\omega:V\to\mathbb F.
$$

An order-two covariant tensor is a bilinear map

$$
B:V\times V\to\mathbb F.
$$

After choosing a basis, it can be represented by a matrix and evaluated as

$$
B(\mathbf u,\mathbf v)
=\mathbf u^{\mathsf T}A\mathbf v.
$$

The Euclidean dot product is a familiar example with $A=I$ in an orthonormal
basis. This illustrates why a tensor may look like a matrix while carrying a
different conceptual role from a linear transformation.

## Axes and order

In coordinate form:

- an order-zero tensor is represented by a scalar;
- an order-one tensor is represented by a vector of components;
- an order-two tensor is represented by a two-axis array;
- higher-order tensors require more coordinate axes.

“Order” here counts tensor slots or axes, not geometric dimension. A vector in
$\mathbb R^{100}$ is still order one; a $3\times3\times3$ array is order three.

In machine learning, the practical word *tensor* commonly refers to such
arrays together with their shape, element type, and computational device.
That usage is extremely useful, but the abstract mathematical content depends
on what the axes mean and how the object transforms.

## Contraction

A contraction pairs compatible tensor slots and sums over the paired index.
Matrix-vector multiplication is a familiar example:

$$
y_i=\sum_j A_{ij}x_j.
$$

The index $j$ disappears after summation, reducing the order of the combined
object. Dot products, traces, and matrix multiplication can all be understood
as contractions.

## The progression

The path from scalars to tensors is compositional:

1. scalars supply coefficients and scales;
2. vectors support addition and scalar multiplication;
3. linear maps preserve that structure and become matrices after bases are
   chosen;
4. tensors encode multilinear relations among several vector or dual spaces.

Arrays are the coordinate surfaces we compute with. The tensor is the
structure those coordinates represent.

