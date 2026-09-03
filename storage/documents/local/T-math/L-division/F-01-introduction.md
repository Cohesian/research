# Division as sharing, measuring, and scaling

The notation

$$
\frac{a}{b},
\qquad b\ne0,
$$

can answer several closely related questions. The arithmetic result may be the
same while the meaning of that result changes with the question.

Two interpretations are especially fundamental:

- **partitive division:** split a quantity into a given number of equal groups;
- **quotative division:** measure how many groups of a given size fit in a
  quantity.

Both are inverse problems for multiplication.

## Partitive division: how much per group?

Suppose twelve objects are shared equally among three groups. If $q$ is the
amount received by each group, then

$$
3q=12.
$$

Solving for $q$ gives

$$
q=\frac{12}{3}=4.
$$

The divisor $3$ counts groups; the quotient $4$ measures objects per group.

In general, the partitive reading of $a/b$ is:

> If a total quantity $a$ is distributed equally among $b$ groups, what is the
> quantity in one group?

It is natural when $b$ is a positive integer, but the algebraic operation
extends beyond literal collections. Dividing a length by $2.5$, for example,
still means scaling it by the reciprocal $1/2.5$ even if “two and a half
groups” is not the most concrete story.

## Quotative division: how many units fit?

Now ask how many groups of size three can be made from twelve objects. If $n$
is the number of groups, then

$$
n(3)=12,
$$

so

$$
n=\frac{12}{3}=4.
$$

The divisor $3$ now measures objects per group; the quotient $4$ counts the
groups.

The general question is:

> How many copies of a quantity $b$ compose the quantity $a$?

This interpretation does not require the quotient to be an integer. For
example,

$$
\frac{5}{2}=2.5
$$

says that two and a half copies of a length-two segment compose a length-five
segment.

Division can also count smaller units:

$$
\frac{12}{0.5}=24.
$$

Twenty-four half-units fit in twelve units. Dividing by a number smaller than
one increases the numerical result because the measuring unit became smaller.

## The same equation, different dimensions

Both readings solve

$$
bq=a.
$$

The symbols alone do not determine the interpretation. Units and context do.

| Question | $a$ | $b$ | $a/b$ |
|---|---|---|---|
| share 12 cookies among 3 groups | cookies | groups | cookies per group |
| form groups of 3 cookies from 12 | cookies | cookies per group | groups |
| travel 12 meters in 3 seconds | meters | seconds | meters per second |

In the last row, division constructs a rate:

$$
\frac{12\ \mathrm{m}}{3\ \mathrm{s}}
=4\ \mathrm{m/s}.
$$

This is neither literally sharing nor counting groups, but it preserves the
same quotient structure: output units are divided by input units.

## Division as multiplication by an inverse

For nonzero $b$,

$$
\frac{a}{b}=a\left(\frac{1}{b}\right)=ab^{-1}.
$$

The reciprocal $b^{-1}$ is the unique number satisfying

$$
bb^{-1}=1.
$$

This view turns division into scaling. First determine the factor that converts
$b$ into one; then apply that factor to $a$.

It also explains equivalent fractions. Multiplying numerator and denominator
by the same nonzero factor $k$ leaves the quotient unchanged:

$$
\frac{a}{b}=\frac{ka}{kb}.
$$

Both numerator and denominator were rescaled, so their relative measurement
did not change.

## One-dimensional vectors

A scalar is a number used as magnitude or scale. A one-dimensional vector can
be written as

$$
\mathbf{v}=a\mathbf{e},
$$

where $\mathbf{e}$ is a chosen basis direction and $a$ is its coordinate.

Dividing the vector by a nonzero scalar acts on its coordinate:

$$
\frac{\mathbf{v}}{b}
=\frac{a}{b}\mathbf{e}.
$$

For example, if

$$
\mathbf{v}=12\mathbf{e},
$$

then sharing it into three equal vector displacements gives

$$
\frac{\mathbf{v}}{3}=4\mathbf{e}.
$$

The quotative view can instead choose $b\mathbf{e}$ as the measuring vector
and ask for the scalar $q$ satisfying

$$
q(b\mathbf{e})=a\mathbf{e}.
$$

Because both vectors lie on the same basis direction,

$$
q=\frac{a}{b}.
$$

In one dimension, coordinates behave like signed scalars, but the distinction
still matters: the vector belongs to a vector space, while the coordinate and
the divisor belong to its scalar field.

## Direction and sign

Signs encode orientation as well as magnitude. In one dimension,

$$
\frac{-12\mathbf{e}}{3}=-4\mathbf{e}
$$

preserves direction, while

$$
\frac{12\mathbf{e}}{-3}=-4\mathbf{e}
$$

reverses it. Dividing by a negative scalar combines magnitude scaling with a
reflection through the origin.

## Why division by zero is undefined

To define $a/0$ through multiplication, we would need a number $q$ such that

$$
0q=a.
$$

If $a\ne0$, no such $q$ exists. If $a=0$, every $q$ satisfies the equation, so
there is no unique answer. Equivalently, zero has no multiplicative inverse.

This is different from limits in which a denominator approaches zero. A limit
studies nearby nonzero values; it does not silently turn division by zero into
a valid arithmetic operation.

## One operation, several projections

The quotient $a/b$ may be projected as:

- a fair share of $a$ across $b$ groups;
- a measurement of $a$ in units of size $b$;
- a ratio comparing two quantities;
- a rate carrying compound units;
- multiplication of $a$ by the inverse scale $b^{-1}$;
- coordinate scaling of a vector.

These are not competing definitions. They are contextual views of the same
algebraic relation

$$
b\left(\frac{a}{b}\right)=a,
\qquad b\ne0.
$$
