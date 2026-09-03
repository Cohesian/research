# The integral as accumulation

A derivative describes local change. An integral combines local contributions
across an interval.

Suppose $v(x)$ is a rate. Partition $[a,b]$ into short subintervals with
widths $\Delta x_i$. On a sufficiently small subinterval, the contribution is
approximately

$$
v(x_i^*)\Delta x_i,
$$

where $x_i^*$ is a sample point inside that subinterval. Adding the
contributions gives a Riemann sum:

$$
\sum_{i=1}^{n}v(x_i^*)\Delta x_i.
$$

The definite integral is the limit of such sums as the largest subinterval
width tends to zero:

$$
\int_a^b v(x)\,dx
=\lim_{\max \Delta x_i\to0}
\sum_{i=1}^{n}v(x_i^*)\Delta x_i.
$$

This is continuous accumulation, not merely multiplication by one fixed rate.

## Reconstructing the change of $x^2$

For

$$
f(x)=x^2,
\qquad
f'(x)=2x,
$$

the accumulated local change from $3$ to $4$ is

$$
\int_3^4 2x\,dx.
$$

Since an antiderivative of $2x$ is $x^2$,

$$
\int_3^4 2x\,dx
=\left[x^2\right]_3^4
=16-9
=7.
$$

The integral returns the change in $f$, not the final value by itself. Starting
from $f(3)=9$,

$$
f(4)=f(3)+\int_3^4 f'(x)\,dx=9+7=16.
$$

This resolves the failure of holding the initial slope constant. The linear
estimate used $6$ throughout the interval and produced $15$. Integration lets
the rate vary continuously from $6$ to $8$, producing the exact change $7$.

## Area and accumulated change

Geometrically, a definite integral is signed area between the graph of the
integrand and the horizontal axis. When the integrand is a rate, this area is
also accumulated change.

These are two readings of the same construction:

- height $\times$ narrow width gives a small area;
- rate $\times$ small input change gives a small output change.

The units agree. If $v$ has units of output per input and $dx$ has units of
input, then $v(x)\,dx$ has units of output.

It is important to distinguish

$$
\int_3^4 2x\,dx=7
$$

from

$$
\int_3^4 x^2\,dx
=\left[\frac{x^3}{3}\right]_3^4
=\frac{37}{3}.
$$

The first integrates the rate of $x^2$ and recovers its change. The second
accumulates the values of $x^2$ themselves and answers a different question.

## Resolution improves the approximation

Using $n$ equal subintervals of width

$$
\Delta x=\frac{b-a}{n},
$$

a left-endpoint approximation is

$$
L_n=\sum_{i=0}^{n-1}v(a+i\Delta x)\Delta x.
$$

For an increasing rate, $L_n$ underestimates the integral. A right-endpoint
sum overestimates it. Both converge toward the same value as $n$ increases.

The integral is therefore not an infinite computation performed one term at a
time. It is a limit that identifies the value approached by increasingly fine
finite approximations.

