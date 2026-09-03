# Finite change: the slope between two observations

Calculus begins with a simple problem: a quantity changes, and we want to
describe that change precisely.

Consider

$$
f(x)=x^2.
$$

At $x=3$, the function has value $9$. At $x=4$, it has value $16$. The input
and output changes are

$$
\Delta x=4-3=1,
\qquad
\Delta y=16-9=7.
$$

Their quotient,

$$
\frac{\Delta y}{\Delta x}=7,
$$

says that the output changed by an average of seven units per unit of input
over the interval $[3,4]$. Geometrically, this is the slope of the secant line
through $(3,9)$ and $(4,16)$.

It is an average across an interval. It is not yet the slope at a single
point.

## The slope changes with the interval

Move to the next unit interval:

$$
f(5)-f(4)=25-16=9.
$$

Then to the next:

$$
f(6)-f(5)=36-25=11.
$$

The successive changes are

$$
7,9,11,\ldots
$$

For a unit step starting at $x$,

$$
f(x+1)-f(x)
=(x+1)^2-x^2
=2x+1.
$$

This formula explains the odd-number pattern. It is the finite difference of
$x^2$ at step size one.

The interval matters. Starting at $x=3$ but using a smaller step $h=0.5$,

$$
\frac{f(3.5)-f(3)}{0.5}
=\frac{12.25-9}{0.5}
=6.5.
$$

The numerator alone is $3.25$, but the slope is $6.5$ because slope compares
output change with input change. Halving the interval does not simply halve
the previous slope: the curve has a different rate at every nearby position.

## The general secant slope

Let the interval begin at an arbitrary $x$ and have nonzero width $h$. The
average rate is

$$
\frac{f(x+h)-f(x)}{h}.
$$

For $f(x)=x^2$,

$$
\begin{aligned}
\frac{(x+h)^2-x^2}{h}
&=\frac{x^2+2xh+h^2-x^2}{h}\\
&=\frac{2xh+h^2}{h}\\
&=2x+h,
\qquad h\ne 0.
\end{aligned}
$$

This is already a generalization. Instead of memorizing a table of slopes,
we have one expression for every starting point $x$ and every nonzero interval
$h$.

For $x=3$ it becomes $6+h$:

| $h$ | secant slope $6+h$ |
|---:|---:|
| $1$ | $7$ |
| $0.5$ | $6.5$ |
| $0.1$ | $6.1$ |
| $0.01$ | $6.01$ |
| $-0.1$ | $5.9$ |

Approaching from either side suggests a stable local value: $6$.

## Secants carry interval-scale knowledge

A secant slope answers:

> Across this chosen interval, how much output change occurred per unit of
> input change?

It depends on two pieces of information: the position $x$ and the scale $h$.
For a straight line, changing $h$ would not change the answer. For a curved
function, it generally does.

Calculus obtains a point-local rate by preserving the position while letting
the interval shrink. That limiting operation produces the derivative.

