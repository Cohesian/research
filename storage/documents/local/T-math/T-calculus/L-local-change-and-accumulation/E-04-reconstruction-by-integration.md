# Reconstruction by Integration

The derivative gives a local rate. The integral accumulates that rate over an interval.

Let $f$ be differentiable on $[a,b]$ with a continuous derivative. The Fundamental Theorem of Calculus states:

$$
f(b)-f(a)
=
\int_a^b f'(x)\,dx.
$$

For:

$$
f(x)=x^2,
\qquad
f'(x)=2x,
$$

the change from $x=3$ to $x=4$ is:

$$
f(4)-f(3)=16-9=7.
$$

Integration reconstructs the same result from the changing local slopes:

$$
\int_3^4 2x\,dx
=
\left[x^2\right]_3^4
=16-9
=7.
$$

## Refine a discrete partition

Divide $[3,4]$ into $n$ equal pieces:

$$
\Delta x=\frac{4-3}{n}=\frac{1}{n}.
$$

Using the left endpoint of each piece:

$$
x_k=3+\frac{k}{n},
\qquad
k=0,1,\ldots,n-1.
$$

The accumulated local estimate is:

$$
S_n
=
\sum_{k=0}^{n-1}f'(x_k)\,\Delta x
=
\sum_{k=0}^{n-1}
2\left(3+\frac{k}{n}\right)\frac{1}{n}.
$$

This simplifies to:

$$
S_n=7-\frac{1}{n}.
$$

Therefore:

$$
\lim_{n\to\infty}S_n=7.
$$

| Number of pieces $n$ | Left accumulation $S_n$ |
| ---: | ---: |
| $1$ | $6$ |
| $2$ | $6.5$ |
| $4$ | $6.75$ |
| $10$ | $6.9$ |
| $100$ | $6.99$ |

The discrete approximation approaches the exact macroscopic change as the widths shrink.

## Where does the curvature go?

For one finite step $h$, the square function changes by:

$$
f(x+h)-f(x)=2xh+h^2.
$$

The first-order contribution is $2xh$. The local error is $h^2$.

Across a unit interval split into $n$ equal steps, $h=1/n$. There are $n$ local quadratic errors, so their total scale is:

$$
n h^2
=
n\left(\frac{1}{n}\right)^2
=
\frac{1}{n}
\to0.
$$

The curvature has not been ignored arbitrarily. Refinement drives the accumulated first-order error to zero.

## Secant slope as an average derivative

The average value of the derivative on $[a,b]$ is:

$$
\frac{1}{b-a}\int_a^b f'(x)\,dx.
$$

By the Fundamental Theorem:

$$
\frac{1}{b-a}\int_a^b f'(x)\,dx
=
\frac{f(b)-f(a)}{b-a}.
$$

The right side is exactly the secant slope.

For $[3,4]$:

$$
\frac{1}{4-3}\int_3^4 2x\,dx=7.
$$

This explains the original observation. The slope seven from $3$ to $4$ is not the local slope at either endpoint:

$$
f'(3)=6,
\qquad
f'(4)=8.
$$

It is the average of all local derivative values across the interval.

The derivative describes how the function changes locally. The integral composes those localized changes into an exact global displacement.
