# Finite Change: Measuring a Curve at One Scale

Consider the function:

$$
f(x)=x^2.
$$

At two neighbouring integers:

$$
f(3)=9,
\qquad
f(4)=16.
$$

The horizontal and vertical changes are:

$$
\Delta x=4-3=1,
\qquad
\Delta y=16-9=7.
$$

Therefore, the slope of the secant line joining the two points is:

$$
\frac{\Delta y}{\Delta x}=\frac{7}{1}=7.
$$

This means that over this particular interval, the output changes by an average of seven output units per input unit.

It does **not** yet say that the curve has slope seven at every point between $3$ and $4$.

## The pattern between consecutive squares

Repeat the same measurement using steps of width one:

$$
f(4)-f(3)=16-9=7,
$$

$$
f(5)-f(4)=25-16=9,
$$

$$
f(6)-f(5)=36-25=11.
$$

The increments are the odd numbers:

$$
7,9,11,\ldots
$$

There is already a general law here. For an arbitrary $x$:

$$
f(x+1)-f(x)
=(x+1)^2-x^2
=2x+1.
$$

The expression $2x+1$ exactly describes the vertical increment produced by a horizontal step of one.

This is a scale-dependent law: its measuring ruler is fixed at $h=1$.

## Replace the fixed ruler by h

Let $h\neq0$ be the horizontal gap. The vertical change from $x$ to $x+h$ is:

$$
\Delta_h f(x)
=f(x+h)-f(x).
$$

For $f(x)=x^2$:

$$
\Delta_h f(x)
=(x+h)^2-x^2
=2xh+h^2.
$$

The corresponding secant slope is the finite-difference quotient:

$$
D_hf(x)
=\frac{f(x+h)-f(x)}{h}.
$$

Substituting the exact change:

$$
D_hf(x)
=\frac{2xh+h^2}{h}
=2x+h.
$$

This formula generalizes every finite scale at once.

At $x=3$:

| $h$ | $\Delta_h f(3)$ | $D_hf(3)$ |
| ---: | ---: | ---: |
| $1$ | $7$ | $7$ |
| $0.5$ | $3.25$ | $6.5$ |
| $0.25$ | $1.5625$ | $6.25$ |
| $0.1$ | $0.61$ | $6.1$ |

The vertical change becomes small because the horizontal interval becomes small. The quotient separates the rate from the interval width and approaches six.

Finite differences are not failed derivatives. They answer a different question: **what is the average rate of change across this nonzero scale $h$?**
