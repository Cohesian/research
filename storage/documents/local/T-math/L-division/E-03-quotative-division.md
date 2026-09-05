# Quotative Division: How Many Units Fit?

Quotative division begins with two magnitudes of the same kind:

- a total magnitude $a$;
- a chosen unit magnitude $b$.

It asks how many copies of $b$ reconstruct $a$.

We seek $c$ such that:

$$
a=cb.
$$

Therefore:

$$
c=\frac{a}{b}.
$$

This time the quotient is a count or ratio rather than the size of one part.

## Measuring by repeated placement

Suppose:

$$
a=10\,\mathrm{mm},
\qquad
b=2\,\mathrm{mm}.
$$

Repeatedly placing the unit $b$ along the total gives:

$$
\underbrace{2\,\mathrm{mm}+2\,\mathrm{mm}+2\,\mathrm{mm}+2\,\mathrm{mm}+2\,\mathrm{mm}}_{5\text{ copies}}
=10\,\mathrm{mm}.
$$

Hence:

$$
\frac{10\,\mathrm{mm}}{2\,\mathrm{mm}}=5.
$$

The units cancel because the quotient compares like with like:

$$
\frac{\mathrm{mm}}{\mathrm{mm}}=1.
$$

The answer is dimensionless: one millimetre-length is being compared with another millimetre-length.

## When the unit does not fit an integer number of times

Let:

$$
c=\frac{a}{b}.
$$

If $c$ is not an integer, write:

$$
c=n+\rho,
\qquad
n=\lfloor c\rfloor,
\qquad
0\leq\rho<1.
$$

Then:

$$
a=nb+\rho b.
$$

This says that $n$ complete copies of $b$ fit inside $a$, followed by a fractional copy $\rho$.

For example:

$$
\frac{10\,\mathrm{cm}}{4\,\mathrm{cm}}=2.5
=2+0.5.
$$

Two complete $4\,\mathrm{cm}$ units account for $8\,\mathrm{cm}$; half of another unit accounts for the remaining $2\,\mathrm{cm}$.

This is related to, but distinct from, integer Euclidean division:

$$
a=nb+r,
\qquad
0\leq r<b.
$$

The remainder $r$ has the same units as $a$ and $b$, whereas $\rho=r/b$ is a dimensionless fraction of one unit.

## The vector boundary

If two vectors lie on the same ray and satisfy:

$$
\vec a=c\vec b,
\qquad
c\geq0,
$$

then $c$ counts how many directed copies of $\vec b$ form $\vec a$.

More generally, comparing magnitudes gives:

$$
c=\frac{\lVert\vec a\rVert}{\lVert\vec b\rVert},
\qquad
\vec b\neq\vec 0.
$$

This quotient compares lengths; it does not define arbitrary vector division and does not say that the vectors share a direction.

## The duality

Partitive and quotative division reverse what is known:

- Partitive: know $a$ and the count $b$; find the size $c$.
- Quotative: know $a$ and the unit size $b$; find the count $c$.

Both are governed by the same reconstruction:

$$
a=bc.
$$

The equation is stable. The interpretation comes from the roles and units assigned to its terms.
