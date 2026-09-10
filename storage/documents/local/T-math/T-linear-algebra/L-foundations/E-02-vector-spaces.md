# Vector Spaces

A vector space is a set $V$ whose elements can be added together and scaled by values from a field $\mathbb{F}$.

If:

$$
\vec u,\vec v\in V,
\qquad
\alpha\in\mathbb{F},
$$

then closure requires:

$$
\vec u+\vec v\in V,
\qquad
\alpha\vec v\in V.
$$

These operations obey compatibility rules: associativity, commutativity of vector addition, a zero vector, additive inverses, distributivity, and compatibility with scalar multiplication.

## A vector is more general than an arrow

In $\mathbb{R}^2$ or $\mathbb{R}^3$, vectors can be visualized as directed displacements. For example:

$$
\vec v=
\begin{bmatrix}
3\\
4
\end{bmatrix}
$$

points from the selected origin toward $(3,4)$.

This geometric picture is powerful, but vectors can also be polynomials, signals, matrices, or functions. For example, the set of polynomials of degree at most two is a vector space:

$$
P_2=\{a+bx+cx^2\mid a,b,c\in\mathbb{R}\}.
$$

Its elements are vectors even though they are not spatial arrows.

## Magnitude and direction require structure

In Euclidean space, a nonzero vector has a magnitude and a direction. The magnitude comes from a norm:

$$
\lVert\vec v\rVert
=
\sqrt{v_1^2+\cdots+v_n^2}.
$$

Angles arise from an inner product:

$$
\vec u\cdot\vec v
=
\lVert\vec u\rVert
\lVert\vec v\rVert
\cos\theta.
$$

An abstract vector space does not automatically include either operation. It first provides addition and scalar multiplication. A norm or inner product enriches that space with geometry.

## Coordinates require a basis

The column:

$$
\begin{bmatrix}
3\\4
\end{bmatrix}
$$

is not the vector in isolation; it is the coordinate representation of the vector relative to an ordered basis.

Using the standard basis:

$$
\vec e_1=
\begin{bmatrix}
1\\0
\end{bmatrix},
\qquad
\vec e_2=
\begin{bmatrix}
0\\1
\end{bmatrix},
$$

we mean:

$$
\vec v=3\vec e_1+4\vec e_2.
$$

The same vector can have different coordinates in another basis. The geometric or abstract object remains; its description changes.
