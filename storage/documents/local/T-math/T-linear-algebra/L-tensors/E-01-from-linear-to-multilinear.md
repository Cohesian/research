# From Linear to Multilinear

A linear map accepts one vector argument and preserves linear combinations:

$$
T:V\to W.
$$

A multilinear map accepts several vector or covector arguments and is linear in each argument while the others are held fixed.

For example, a bilinear map:

$$
B:V\times V\to\mathbb{F}
$$

satisfies:

$$
B(\alpha\vec u+\beta\vec v,\vec w)
=
\alpha B(\vec u,\vec w)
+
\beta B(\vec v,\vec w),
$$

and obeys an analogous rule in its second argument.

## Covectors

A covector is a linear map from vectors to scalars:

$$
\omega:V\to\mathbb{F}.
$$

The collection of all covectors forms the dual space $V^*$.

If $\omega\in V^*$ and $\vec v\in V$, their natural pairing is:

$$
\omega(\vec v)\in\mathbb{F}.
$$

Vectors and covectors transform differently under a change of basis. This distinction becomes essential for tensors.

## Tensor products

Given vectors $\vec u\in U$ and $\vec v\in V$, their tensor product:

$$
\vec u\otimes\vec v
$$

is not vector addition and is not a dot product. It constructs an object that preserves the independent linear participation of both factors.

Tensor spaces are built from products of vector spaces and dual spaces. A tensor can equivalently be described as an element of such a tensor-product space or as an appropriate multilinear map.

## Orders zero, one, and two

- A scalar is an order-zero tensor.
- A vector or covector is an order-one tensor.
- A bilinear form is an order-two tensor.
- A linear operator $V\to V$ can be represented as a mixed order-two tensor with one vector and one covector direction.

This hierarchy is more precise than saying that a tensor is merely an array with more axes.
