# The derivative as local change

The derivative extracts a local rate from finite comparisons. For a function
$f$, its derivative at $x$ is

$$
f'(x)=\lim_{h\to 0}\frac{f(x+h)-f(x)}{h},
$$

when this limit exists.

The quotient is evaluated only for $h\ne0$. The notation $h\to0$ does not ask
us to divide by zero; it asks what value the quotient approaches as nonzero
intervals become arbitrarily small.

## Deriving the derivative of $x^2$

For $f(x)=x^2$, the finite-change calculation gives

$$
\frac{f(x+h)-f(x)}{h}=2x+h.
$$

Taking the limit removes the remaining interval dependence:

$$
\begin{aligned}
f'(x)
&=\lim_{h\to0}(2x+h)\\
&=2x.
\end{aligned}
$$

Thus the derivative is not a long table of unrelated slopes. It is another
function,

$$
f'(x)=2x,
$$

that assigns a local rate to every input.

At $x=3$,

$$
f'(3)=6.
$$

At $x=4$,

$$
f'(4)=8.
$$

The secant from $3$ to $4$ had slope $7$, exactly between the endpoint
derivatives in this quadratic example. The curve begins that interval with
local slope $6$ and ends it with local slope $8$.

## Local linearization

Near a differentiable point, a curved function behaves approximately like a
line. For a small displacement $\Delta x$,

$$
f(x+\Delta x)
\approx f(x)+f'(x)\Delta x.
$$

For $x^2$ this becomes

$$
(x+\Delta x)^2
\approx x^2+2x\Delta x.
$$

The exact identity is

$$
(x+\Delta x)^2
=x^2+2x\Delta x+(\Delta x)^2.
$$

The linear approximation omits $(\Delta x)^2$. As $\Delta x$ shrinks, that
error becomes small even faster than $\Delta x$ itself.

At $x=3$ and $\Delta x=0.01$,

$$
f(3)+f'(3)(0.01)=9+6(0.01)=9.06,
$$

while

$$
f(3.01)=9.0601.
$$

The difference is $0.0001=(0.01)^2$.

This is one of the derivative's deepest meanings: $f'(x)$ is the best local
linear coefficient for $f$ at $x$.

## Differentials and units

The expression

$$
df=f'(x)\,dx
$$

records the linear part of a small output change. For $f(x)=x^2$,

$$
df=2x\,dx.
$$

If $x$ is measured in meters and $f(x)$ in square meters, then $f'(x)$ has
units of meters: square meters of output change per meter of input change.
Units help expose whether a derivative has been interpreted consistently.

## Local does not mean constant

The value $f'(3)=6$ describes change infinitesimally near $3$. Extending that
slope unchanged across the whole interval $[3,4]$ predicts

$$
9+6(1)=15,
$$

but the exact endpoint is $16$. The missing unit appears because the local
slope itself changes as $x$ moves.

To reconstruct a finite change from continuously varying local rates, those
rates must be accumulated. That is the role of the integral.

