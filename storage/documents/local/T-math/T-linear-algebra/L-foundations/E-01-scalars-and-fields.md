# Scalars and Fields

A scalar is a value used to measure, weight, or scale another object. In real linear algebra, scalars usually belong to the field of real numbers:

$$
\alpha\in\mathbb{R}.
$$

In complex linear algebra, they belong to:

$$
\alpha\in\mathbb{C}.
$$

The word *scalar* describes the role played by the value inside a vector space. The number $3$ may represent three metres, three seconds, a probability weight, or a scale factor. Its semantics come from the model; its algebra comes from the selected field.

## Why a field?

A field supports addition, subtraction, multiplication, and division by nonzero values. These operations make it possible to form expressions such as:

$$
\alpha\vec v+\beta\vec w.
$$

The field supplies the coefficients $\alpha$ and $\beta$. The vector space supplies the objects $\vec v$ and $\vec w$ being combined.

## Scalar multiplication

Given a vector $\vec v$ and a scalar $\alpha$:

$$
\alpha\vec v
$$

is another vector in the same vector space.

In Euclidean geometry:

- $|\alpha|>1$ stretches the vector;
- $0<|\alpha|<1$ contracts it;
- $\alpha=0$ collapses it to the zero vector;
- $\alpha<0$ also reverses its direction.

If a norm is available, scalar multiplication obeys:

$$
\lVert\alpha\vec v\rVert
=
|\alpha|\,\lVert\vec v\rVert.
$$

## Scalars are coordinate-independent

A vector can acquire different coordinate lists under different bases. A scalar value does not acquire an additional directional axis under a basis change. This is why a scalar can be understood as an order-zero quantity.

This does not mean scalars are meaningless raw numbers. It means they carry no vector-space direction of their own. Their meaning may still include units, constraints, probability, energy, temperature, or any other modeled quantity.

## The first compositional step

Linear algebra begins composing structure when scalars weight vectors:

$$
\alpha_1\vec v_1+\cdots+\alpha_n\vec v_n.
$$

This expression is a linear combination. It is the mechanism behind coordinates, matrix multiplication, span, basis, and eventually tensor contraction.
