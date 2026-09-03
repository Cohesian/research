# Visual laboratory: finite steps approaching continuous change

This laboratory accompanies the notebook with the same rooted path. Its goal
is to make three related objects visible for

$$
f(x)=x^2:
$$

1. secant lines across finite intervals;
2. the tangent obtained as the interval shrinks;
3. Riemann sums converging to an integral.

The notebook uses Python with NumPy and Matplotlib. It stores no generated
outputs, so executing it remains the reproducible source of its figures.

## Experiment 1: shrinking the secant interval

Fix $x_0=3$ and compare

$$
m(h)=\frac{f(x_0+h)-f(x_0)}{h}=2x_0+h.
$$

The notebook plots the secant line for several positive values of $h$ and the
tangent line with slope

$$
f'(x_0)=2x_0=6.
$$

As $h$ decreases, the second point approaches the first and the secant slope
approaches six. The limiting tangent is local: it matches the curve most
closely near $x_0$, not across the entire plot.

## Experiment 2: approximation error

The exact change is

$$
f(x_0+h)-f(x_0)=2x_0h+h^2.
$$

The derivative predicts only the linear part $2x_0h$. The omitted error is

$$
E(h)=h^2.
$$

A log-log graph of $E(h)$ against $|h|$ has slope two. This is visual evidence
that halving $h$ divides the error by four.

## Experiment 3: accumulating the derivative

The notebook approximates

$$
\int_3^4 2x\,dx
$$

with left and right Riemann sums. Because $2x$ is increasing, the left sums
approach seven from below and the right sums approach it from above.

The exact endpoint is then reconstructed as

$$
f(4)=f(3)+\int_3^4 2x\,dx=9+7=16.
$$

## What the experiment does and does not show

The figures demonstrate convergence for one smooth function and selected
numerical resolutions. They do not prove the general theorems of calculus.
Their purpose is to connect the symbols to observable geometric behavior:

- finite comparisons depend on interval size;
- a derivative is their stable local limit;
- an integral is the limit of increasingly fine accumulated contributions;
- the Fundamental Theorem connects those two limits.
