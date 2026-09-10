# Linear Combinations

Given vectors $\vec v_1,\ldots,\vec v_n$ and scalars $\alpha_1,\ldots,\alpha_n$, an expression of the form:

$$
\alpha_1\vec v_1+\cdots+\alpha_n\vec v_n
$$

is a linear combination.

This is the central compositional operation of linear algebra: select vectors, scale each one, and add the results.

## Span

The span of a collection of vectors contains every linear combination that can be generated from them:

$$
\operatorname{span}\{\vec v_1,\ldots,\vec v_n\}
=
\left\{
\sum_{i=1}^{n}\alpha_i\vec v_i
\;\middle|\;
\alpha_i\in\mathbb{F}
\right\}.
$$

For the standard vectors in $\mathbb{R}^2$:

$$
\operatorname{span}\{\vec e_1,\vec e_2\}=\mathbb{R}^2.
$$

If only $\vec e_1$ is available, the span is the horizontal line through the origin.

## Linear independence

The vectors $\vec v_1,\ldots,\vec v_n$ are linearly independent when:

$$
\alpha_1\vec v_1+\cdots+\alpha_n\vec v_n=\vec0
$$

implies:

$$
\alpha_1=\cdots=\alpha_n=0.
$$

No vector in an independent collection can be reconstructed from the others. Each one contributes a genuinely new direction in the algebraic sense.

## Basis

A basis of $V$ is a linearly independent collection that spans $V$.

Therefore every $\vec v\in V$ has one unique coordinate expansion:

$$
\vec v
=
x_1\vec b_1+\cdots+x_n\vec b_n.
$$

The coordinate vector is:

$$
[\vec v]_{\mathcal B}
=
\begin{bmatrix}
x_1\\
\vdots\\
x_n
\end{bmatrix}.
$$

The coefficients are not additional pieces attached to the vector. They are its description relative to the ordered basis $\mathcal B=(\vec b_1,\ldots,\vec b_n)$.

## Subspaces

A subset $W\subseteq V$ is a subspace when it contains the zero vector and is closed under vector addition and scalar multiplication.

Every span is a subspace:

$$
W=\operatorname{span}\{\vec v_1,\ldots,\vec v_k\}.
$$

Its dimension is the number of vectors in any basis of $W$.

This language prepares the path from vectors to matrices. The columns of a matrix generate its image through exactly the same operation: linear combination.
