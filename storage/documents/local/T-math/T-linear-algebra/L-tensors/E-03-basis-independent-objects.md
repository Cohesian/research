# Basis-Independent Objects

A tensor exists independently of a particular coordinate system. Its components change when the basis changes, but the underlying multilinear object does not.

This is the same distinction already encountered with vectors:

- the vector is the object;
- a coordinate column is its description in one basis.

For tensors, the number of indices makes the component transformation richer.

## A bilinear form

Consider a bilinear form:

$$
B:V\times V\to\mathbb{F}.
$$

After choosing a basis, it can be represented by a matrix $G$ so that:

$$
B(\vec u,\vec v)
=
[\vec u]^{\mathsf T}G[\vec v].
$$

Under a change of coordinates:

$$
[\vec v]=P[\vec v]_{\mathrm{new}},
$$

the component matrix becomes:

$$
G_{\mathrm{new}}=P^{\mathsf T}GP.
$$

The entries change, but the scalar produced by $B(\vec u,\vec v)$ remains the same when every component is transformed consistently.

## A linear operator

For a linear operator $A:V\to V$, the component matrix instead changes by similarity:

$$
A_{\mathrm{new}}=P^{-1}AP.
$$

These two transformation laws differ because a bilinear form and a linear operator have different tensor types, even though both can appear as square matrices in coordinates.

## Why the distinction matters

Calling every multidimensional array a tensor hides the invariant structure. The mathematical object is characterized by:

- the spaces from which its arguments come;
- whether each slot is vector-like or covector-like;
- multilinearity in those slots;
- the rule by which components change with the basis.

An array is a useful implementation and visualization. The tensor is the relationship that survives a valid change of coordinates.
