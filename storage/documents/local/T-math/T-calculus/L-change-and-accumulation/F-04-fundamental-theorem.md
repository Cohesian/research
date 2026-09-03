# The Fundamental Theorem: change and accumulation are inverse views

Differentiation and integration seem to ask opposite questions:

- differentiation starts with a total quantity and extracts its local rate;
- integration starts with a local rate and accumulates its total change.

The Fundamental Theorem of Calculus makes this relationship precise.

## Accumulation creates an antiderivative

Let $v$ be continuous and define

$$
A(x)=\int_a^x v(t)\,dt.
$$

The function $A(x)$ records how much of $v$ has accumulated between a fixed
origin $a$ and the current endpoint $x$. If the endpoint moves by a small
amount $h$, then

$$
A(x+h)-A(x)=\int_x^{x+h}v(t)\,dt.
$$

Over a very short interval, $v(t)$ is close to $v(x)$, so

$$
\frac{A(x+h)-A(x)}{h}\approx v(x).
$$

Taking the limit gives

$$
A'(x)=v(x).
$$

The derivative of accumulated change is the rate being accumulated.

## Integrating a derivative recovers net change

If $F'(x)=v(x)$, then

$$
\int_a^b v(x)\,dx=F(b)-F(a).
$$

Equivalently,

$$
\int_a^b F'(x)\,dx=F(b)-F(a).
$$

For $F(x)=x^2$,

$$
\int_3^4 F'(x)\,dx
=\int_3^4 2x\,dx
=F(4)-F(3)
=7.
$$

## Why the constant disappears and returns

Every function in the family

$$
F(x)=x^2+C
$$

has derivative $2x$. Differentiation erases vertical position because a
constant contributes no change:

$$
\frac{d}{dx}C=0.
$$

An indefinite integral therefore recovers a family:

$$
\int 2x\,dx=x^2+C.
$$

A starting value selects one member. If $F(3)=9$, then $C=0$. If instead
$F(3)=14$, then $C=5$. The local rate is identical, but the global vertical
placement differs.

## Generalization rather than memorization

A finite table might store

$$
f(3)=9,\quad f(3.5)=12.25,\quad f(4)=16.
$$

That table answers only the sampled inputs. The derivative $f'(x)=2x$
describes the local rule everywhere in the domain, and integration transports
that rule across any interval.

This is a useful distinction:

- samples preserve selected observations;
- a derivative encodes a local transformation rule;
- an integral composes those local changes into a finite result.

Neither discrete samples nor continuous laws are universally superior. A
sample is what an experiment observes; a law is a compact model inferred from
structure. Calculus explains how a continuously varying local rule can account
for the global differences between observations.

