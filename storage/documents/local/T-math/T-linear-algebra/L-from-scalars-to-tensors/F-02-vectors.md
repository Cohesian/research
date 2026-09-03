# Vectors: directed change and linear composition

A vector is an element of a vector space: a collection whose elements can be
added together and scaled while obeying consistent algebraic rules.

In $\mathbb{R}^n$, a vector is represented by an ordered coordinate tuple,

$$
\mathbf v=
\begin{bmatrix}
v_1\\
\vdots\\
v_n
\end{bmatrix},
$$

but the coordinate tuple depends on a basis. The vector itself may represent a
displacement, velocity, force, signal, state, or any object with the same
linear structure.

## Addition and scalar multiplication

Vector addition composes directed changes:

$$
\begin{bmatrix}a_1\\a_2\end{bmatrix}
+
\begin{bmatrix}b_1\\b_2\end{bmatrix}
=
\begin{bmatrix}a_1+b_1\\a_2+b_2\end{bmatrix}.
$$

Scalar multiplication scales every coordinate:

$$
\alpha
\begin{bmatrix}v_1\\v_2\end{bmatrix}
=
\begin{bmatrix}\alpha v_1\\\alpha v_2\end{bmatrix}.
$$

These operations interact distributively:

$$
\alpha(\mathbf u+\mathbf v)
=\alpha\mathbf u+\alpha\mathbf v.
$$

This compatibility is the core grammar of a vector space.

## Points and displacements

Coordinates often represent points, but subtracting two points produces a
displacement vector. Given points $\mathbf a$ and $\mathbf b$,

$$
\mathbf d=\mathbf b-\mathbf a
$$

points from $\mathbf a$ toward $\mathbf b$.

The line segment between them is parameterized by

$$
\mathbf p(t)=\mathbf a+t(\mathbf b-\mathbf a),
\qquad 0\le t\le1.
$$

At $t=0$ it returns $\mathbf a$; at $t=1$ it returns $\mathbf b$. At
$t=\tfrac12$ it gives the midpoint:

$$
\mathbf m
=\mathbf a+\frac12(\mathbf b-\mathbf a)
=\frac{\mathbf a+\mathbf b}{2}.
$$

The two formulas are identical. The first emphasizes movement from a local
origin; the second emphasizes symmetry between the endpoints.

## Length and normalization

The Euclidean norm is

$$
\|\mathbf v\|
=\sqrt{\mathbf v\cdot\mathbf v}
=\sqrt{v_1^2+\cdots+v_n^2}.
$$

For $\mathbf v\ne\mathbf0$, its normalized direction is

$$
\widehat{\mathbf v}=\frac{\mathbf v}{\|\mathbf v\|}.
$$

Normalization factors magnitude from direction:

$$
\mathbf v=\|\mathbf v\|\widehat{\mathbf v}.
$$

For example,

$$
\mathbf v=\begin{bmatrix}3\\4\end{bmatrix},
\qquad
\|\mathbf v\|=5,
\qquad
\widehat{\mathbf v}=\begin{bmatrix}3/5\\4/5\end{bmatrix}.
$$

The zero vector cannot be normalized because it has no direction and division
by its zero norm is undefined.

## Dot product, angle, and projection

The Euclidean dot product is

$$
\mathbf u\cdot\mathbf v
=u_1v_1+\cdots+u_nv_n.
$$

It connects coordinates with geometry:

$$
\mathbf u\cdot\mathbf v
=\|\mathbf u\|\|\mathbf v\|\cos\theta.
$$

Consequently:

- a positive dot product indicates an acute relative angle;
- zero indicates orthogonality for nonzero vectors;
- a negative value indicates an obtuse relative angle.

The scalar component of $\mathbf v$ along a unit vector $\widehat{\mathbf u}$
is

$$
\mathbf v\cdot\widehat{\mathbf u},
$$

and the vector projection is

$$
\operatorname{proj}_{\mathbf u}(\mathbf v)
=\frac{\mathbf v\cdot\mathbf u}{\mathbf u\cdot\mathbf u}\mathbf u.
$$

The quotient determines how many scalar units of $\mathbf u$ best align with
$\mathbf v$; multiplication by $\mathbf u$ returns that measurement to vector
space.

## Span and subspaces

The span of vectors $\mathbf v_1,\ldots,\mathbf v_k$ is the set of all their
linear combinations:

$$
\operatorname{span}\{\mathbf v_1,\ldots,\mathbf v_k\}
=\left\{\sum_{i=1}^{k}\alpha_i\mathbf v_i:\alpha_i\in\mathbb F\right\}.
$$

This span is a subspace. A basis is a nonredundant generating set: it spans the
space and is linearly independent. Once a basis is chosen, every vector has a
unique coordinate representation.

