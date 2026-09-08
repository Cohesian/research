# The Derivative: Removing the Measuring Gap

For a finite gap $h\neq0$, the secant slope of $f$ at $x$ is:

$$
D_hf(x)
=
\frac{f(x+h)-f(x)}{h}.
$$

For $f(x)=x^2$, we found:

$$
D_hf(x)=2x+h.
$$

Every chosen value of $h$ leaves its scale inside the answer. To discover a law attached only to the point $x$, calculus asks what value these slopes approach as the gap is made arbitrarily small.

## No smallest positive gap is required

In standard real calculus, there is no smallest positive real number. The notation:

$$
h\to0
$$

does not mean substituting $h=0$ into a quotient that forbids it. It means considering nonzero values of $h$ that can be made closer to zero than any prescribed positive tolerance.

The derivative is defined by the limit:

$$
f'(x)
=
\lim_{h\to0}
\frac{f(x+h)-f(x)}{h},
$$

when that limit exists.

For the square function:

$$
f'(x)
=
\lim_{h\to0}(2x+h)
=2x.
$$

At $x=3$:

$$
f'(3)=6.
$$

The secant slopes $7$, $6.5$, $6.25$, and $6.1$ were not random approximations. They were values of the exact family:

$$
D_hf(3)=6+h,
$$

converging to six as $h\to0$.

## What does the local slope mean?

The number $f'(3)=6$ is a rate. Close to $x=3$, a small horizontal displacement $h$ produces approximately:

$$
\Delta y\approx 6h.
$$

It would be incorrect to say that every displacement from $3$ to $4$ uses the constant slope six. That would produce:

$$
9+6(1)=15,
$$

while the true value is $16$.

The missing unit comes from curvature. The exact increment is:

$$
f(x+h)-f(x)=2xh+h^2.
$$

At $x=3$:

$$
f(3+h)-f(3)=6h+h^2.
$$

The derivative captures the linear term $6h$. The remainder $h^2$ becomes smaller relative to $h$ as the scale shrinks:

$$
\frac{h^2}{h}=h\to0.
$$

This is the precise sense in which a differentiable curve becomes locally linear.

## The tangent line

The local linear model at a point $x_0$ is:

$$
L_{x_0}(x)
=
f(x_0)+f'(x_0)(x-x_0).
$$

For $x_0=3$:

$$
L_3(x)=9+6(x-3).
$$

The tangent line is not the curve. It is the first-order model whose error becomes negligible compared with the displacement as $x\to3$.
