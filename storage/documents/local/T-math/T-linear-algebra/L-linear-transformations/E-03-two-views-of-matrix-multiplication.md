# Two Views of Matrix–Vector Multiplication

Let:

$$
A=
\begin{bmatrix}
a_{11}&a_{12}&\cdots&a_{1n}\\
a_{21}&a_{22}&\cdots&a_{2n}\\
\vdots&\vdots&\ddots&\vdots\\
a_{m1}&a_{m2}&\cdots&a_{mn}
\end{bmatrix},
\qquad
\vec x=
\begin{bmatrix}
x_1\\x_2\\\vdots\\x_n
\end{bmatrix}.
$$

There is one multiplication $A\vec x$, but it has two complementary readings.

## Column view: synthesize the output

Write the matrix by columns:

$$
A=
\begin{bmatrix}
|&|&&|\\
\vec a_1&\vec a_2&\cdots&\vec a_n\\
|&|&&|
\end{bmatrix}.
$$

Then:

$$
A\vec x
=
x_1\vec a_1+
x_2\vec a_2+
\cdots+
x_n\vec a_n.
$$

Each input coordinate scales its corresponding column. The scaled columns are then added.

Because $\vec a_j=A\vec e_j$, this is the same as:

$$
A\vec x
=
A(x_1\vec e_1+\cdots+x_n\vec e_n)
=
x_1A\vec e_1+\cdots+x_nA\vec e_n.
$$

The output must lie in the span of the columns.

## Row view: compute each output coordinate

Write the rows as $\vec r_1^{\mathsf T},\ldots,\vec r_m^{\mathsf T}$. Then:

$$
A\vec x
=
\begin{bmatrix}
\vec r_1\cdot\vec x\\
\vec r_2\cdot\vec x\\
\vdots\\
\vec r_m\cdot\vec x
\end{bmatrix}.
$$

The $i$-th output coordinate is:

$$
(A\vec x)_i
=
\sum_{j=1}^{n}a_{ij}x_j.
$$

Each row acts as a linear measurement of the input.

## One numerical example

Let:

$$
A=
\begin{bmatrix}
2&-1\\
1&2
\end{bmatrix},
\qquad
\vec x=
\begin{bmatrix}3\\4\end{bmatrix}.
$$

Column view:

$$
A\vec x
=
3\begin{bmatrix}2\\1\end{bmatrix}
+
4\begin{bmatrix}-1\\2\end{bmatrix}
=
\begin{bmatrix}2\\11\end{bmatrix}.
$$

Row view:

$$
A\vec x
=
\begin{bmatrix}
(2)(3)+(-1)(4)\\
(1)(3)+(2)(4)
\end{bmatrix}
=
\begin{bmatrix}2\\11\end{bmatrix}.
$$

The column view explains which transformed directions compose the answer. The row view explains how each coordinate of that answer is measured.
