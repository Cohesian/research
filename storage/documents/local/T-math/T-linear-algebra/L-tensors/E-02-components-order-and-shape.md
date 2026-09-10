# Components, Order, and Shape

Once bases are chosen, tensors acquire indexed components.

A vector has one index:

$$
v^i.
$$

A covector also has one index, conventionally written in a lower position:

$$
\omega_i.
$$

An order-two tensor may have components such as:

$$
T^{ij},
\qquad
T^i{}_j,
\qquad
T_{ij},
$$

depending on whether its factors are vector-like or covector-like.

## Why arrays appear

If a vector space has dimension $n$, one vector requires $n$ coordinates. An order-two tensor may require an $n\times n$ component table. An order-three tensor may require an $n\times n\times n$ component block.

This produces familiar storage shapes:

```text
scalar          one component
vector          n components
order 2         n × n components
order 3         n × n × n components
```

But the array is only the coordinate representation after bases have been selected.

## Order is not dimension

Tensor order counts the number of vector or covector slots. Dimension counts the number of basis directions available to each slot.

An order-three tensor over a two-dimensional vector space may have shape:

$$
2\times2\times2.
$$

An order-two tensor between different spaces may have a rectangular shape:

$$
m\times n.
$$

Therefore “three-dimensional array” and “tensor on a three-dimensional vector space” are different statements.

## Outer products and contraction

For column vectors $\vec u\in\mathbb{R}^m$ and $\vec v\in\mathbb{R}^n$, the outer product:

$$
\vec u\vec v^{\mathsf T}
$$

has components:

$$
(\vec u\vec v^{\mathsf T})_{ij}=u_iv_j.
$$

It builds an order-two object from two order-one objects.

Contraction performs the complementary operation of pairing one vector-like index with one covector-like index and summing:

$$
y^i=A^i{}_j x^j.
$$

In coordinates, ordinary matrix-vector multiplication is a contraction over the repeated index $j$.
