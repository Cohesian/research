# Vector Addition and Subtraction

Let:

$$
\vec u=
\begin{bmatrix}
u_1\\u_2
\end{bmatrix},
\qquad
\vec v=
\begin{bmatrix}
v_1\\v_2
\end{bmatrix}.
$$

Their sum is computed coordinate by coordinate:

$$
\vec u+\vec v
=
\begin{bmatrix}
u_1+v_1\\
u_2+v_2
\end{bmatrix}.
$$

Geometrically, addition composes displacements. Travel by $\vec u$, then travel by $\vec v$; the resulting displacement is $\vec u+\vec v$.

Because addition is commutative, the same endpoint appears when the order is reversed:

$$
\vec u+\vec v=\vec v+\vec u.
$$

This produces the familiar parallelogram construction.

## Subtraction as relative displacement

Subtraction adds an inverse:

$$
\vec v-\vec u
=
\vec v+(-\vec u).
$$

When $\vec u$ and $\vec v$ are position vectors from a common origin, the difference:

$$
\vec d=\vec v-\vec u
$$

is the displacement pointing from the tip of $\vec u$ to the tip of $\vec v$.

If points $A$ and $B$ have position vectors $\vec a$ and $\vec b$, then:

$$
\overrightarrow{AB}=\vec b-\vec a.
$$

The order determines direction:

$$
\overrightarrow{BA}=\vec a-\vec b=-\overrightarrow{AB}.
$$

## The midpoint

The midpoint between $A$ and $B$ has position vector:

$$
\vec m=\frac{\vec a+\vec b}{2}.
$$

The same point can be reached by moving halfway from $A$ toward $B$:

$$
\vec m
=
\vec a+\frac{1}{2}(\vec b-\vec a).
$$

Expanding verifies the equivalence:

$$
\vec a+\frac{1}{2}\vec b-\frac{1}{2}\vec a
=
\frac{1}{2}\vec a+\frac{1}{2}\vec b
=
\frac{\vec a+\vec b}{2}.
$$

This identity connects three basic operations: subtraction identifies the relative displacement, scalar multiplication selects half of it, and addition relocates that half-displacement at $A$.
