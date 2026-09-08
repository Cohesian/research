# A Field of Local Rules

The derivative of:

$$
f(x)=x^2
$$

is not one constant slope. It is another function:

$$
f'(x)=2x.
$$

This derivative assigns a local rate to every position in the domain:

$$
x\longmapsto 2x.
$$

For example:

| Position $x$ | Local rate $f'(x)$ |
| ---: | ---: |
| $0$ | $0$ |
| $1$ | $2$ |
| $2$ | $4$ |
| $3$ | $6$ |
| $4$ | $8$ |

Rather than memorizing every secant slope between every possible pair of points, we now have a local law that generates the rate at any point.

## Local linear instructions

At each position $x$, the derivative gives the first-order instruction:

$$
f(x+dx)-f(x)\approx f'(x)\,dx.
$$

For the square function:

$$
df\approx 2x\,dx.
$$

This notation should be read carefully. The derivative supplies a rate, and multiplying by a small width supplies a small predicted change.

Slope alone cannot be accumulated as height. Its units are:

$$
\frac{\text{output units}}{\text{input unit}}.
$$

Multiplying by an input width restores output units:

$$
\frac{\text{output}}{\text{input}}
\times
\text{input}
=
\text{output}.
$$

## The curve as a compatible global shape

Suppose we begin only with the local rule:

$$
\frac{dy}{dx}=2x.
$$

Every function of the form:

$$
y=x^2+C
$$

satisfies that rule, because the derivative of the constant $C$ is zero.

One known value fixes the vertical placement. If:

$$
y(0)=0,
$$

then $C=0$, and the compatible global curve is:

$$
y=x^2.
$$

The derivative therefore preserves local variation but forgets an additive constant. A local law plus one anchor value can reconstruct the global function.

## From microscopic rules to macroscopic change

The phrase “add the local slopes” is incomplete. To move across an interval, each sampled slope must first act over a small width:

$$
f'(x_k)\,\Delta x.
$$

Adding these local contributions produces an approximation:

$$
\Delta f
\approx
\sum_k f'(x_k)\,\Delta x.
$$

As the partition is refined, this sum becomes an integral. The next essay makes that reconstruction explicit.
