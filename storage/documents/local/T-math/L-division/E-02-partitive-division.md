# Partitive Division: The Size of One Equal Part

Partitive division begins with a total and a requested number of equal parts.

Let $a>0$ be a magnitude and let $b\in\mathbb{N}$ with $b>0$. We seek a common part size $c$ such that:

$$
\underbrace{c+c+\cdots+c}_{b\text{ equal parts}}=a.
$$

Because the left side is $bc$,

$$
bc=a
\quad\Longrightarrow\quad
c=\frac{a}{b}.
$$

The quotient is therefore the magnitude carried by one part.

## Partitioning a segment

Represent the total $a$ by the interval $[0,a]$. Define the boundary points:

$$
x_k=\frac{ka}{b},
\qquad
k=0,1,\ldots,b.
$$

The $k$-th part is:

$$
I_k=[x_{k-1},x_k].
$$

Every part has the same length:

$$
\lvert I_k\rvert
=x_k-x_{k-1}
=\frac{ka}{b}-\frac{(k-1)a}{b}
=\frac{a}{b}.
$$

There are $b+1$ boundary points, $b$ equal pieces, and $b-1$ interior cuts. This vocabulary matters: dividing a segment into five pieces normally requires four interior cuts.

## The vector view

Let $\vec a$ be a vector whose magnitude is the total length. One equal directed part is:

$$
\vec c=\frac{1}{b}\vec a.
$$

Positive scalar multiplication preserves direction and scales magnitude:

$$
\lVert\vec c\rVert
=
\left\lVert\frac{1}{b}\vec a\right\rVert
=
\frac{1}{b}\lVert\vec a\rVert.
$$

Repeating that part $b$ times reconstructs the original vector:

$$
\underbrace{\vec c+\vec c+\cdots+\vec c}_{b\text{ times}}
=b\vec c
=b\left(\frac{1}{b}\vec a\right)
=\vec a.
$$

Division by $b$ is therefore a reciprocal scaling by $1/b$.

## One centimetre divided into five parts

Start with:

$$
a=1\,\mathrm{cm},
\qquad
b=5.
$$

Then:

$$
c=\frac{1\,\mathrm{cm}}{5}=0.2\,\mathrm{cm}.
$$

We may change the unit before dividing:

$$
1\,\mathrm{cm}=10\,\mathrm{mm},
$$

so:

$$
\frac{10\,\mathrm{mm}}{5}=2\,\mathrm{mm}.
$$

These are the same physical length because:

$$
2\,\mathrm{mm}=0.2\,\mathrm{cm}.
$$

Changing from centimetres to millimetres enlarges the numerical coordinate by a factor of ten; converting back shrinks it by the same factor. The segment itself never changes. Only its numerical description does.

Partitive division answers the local question hidden inside the whole: **what magnitude does one of the equal parts carry?**
