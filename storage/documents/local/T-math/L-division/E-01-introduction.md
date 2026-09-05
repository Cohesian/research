# Division as Reconstruction

Division is often introduced as a procedure: take two numbers, apply a rule, and obtain a result. A more useful starting point is to treat it as a question about multiplication.

For $b \neq 0$,

$$
c = \frac{a}{b}
\quad\Longleftrightarrow\quad
a = bc.
$$

The quotient $c$ is the value that reconstructs $a$ when multiplied by $b$.

This single equation supports two different questions:

1. If a total $a$ is distributed into $b$ equal parts, how large is each part?
2. If each part has size $b$, how many such parts fit inside $a$?

The arithmetic can be identical while the roles of the quantities are different.

## Two readings of the same notation

### Partitive division

Suppose $12\,\mathrm{m}$ is divided into $3$ equal parts:

$$
\frac{12\,\mathrm{m}}{3}
=
4\,\mathrm{m}.
$$

Here:

- $12\,\mathrm{m}$ is the total length;
- $3$ is a dimensionless number of equal parts;
- $4\,\mathrm{m}$ is the length of one part.

The question is: **how much belongs to one part?**

### Quotative division

Suppose instead that the total is $12\,\mathrm{m}$ and one measuring unit is $3\,\mathrm{m}$:

$$
\frac{12\,\mathrm{m}}{3\,\mathrm{m}}
=
4.
$$

Here:

- $12\,\mathrm{m}$ is the total length;
- $3\,\mathrm{m}$ is the size of one unit;
- $4$ is the dimensionless number of copies that fit.

The question is: **how many units fit inside the total?**

## The units reveal the question

The notation $a/b$ does not by itself say which interpretation is intended. Units often reveal it:

| Reading | Numerator | Denominator | Quotient |
| --- | --- | --- | --- |
| Partitive | total magnitude | number of parts | magnitude per part |
| Quotative | total magnitude | magnitude per unit | number of units |

In both cases, multiplication checks the answer:

$$
4\,\mathrm{m}\times 3 = 12\,\mathrm{m},
$$

or:

$$
4\times 3\,\mathrm{m} = 12\,\mathrm{m}.
$$

The factors exchange semantic roles, but the reconstruction law remains the same.

## A geometric boundary

A directed vector does not generally support division by another vector. In this lecture, vector diagrams represent non-negative scalar lengths. If

$$
a=\lVert\vec a\rVert,
$$

then dividing $a$ means dividing the magnitude represented by the segment. Scaling the vector by a scalar is well-defined:

$$
\frac{1}{b}\vec a.
$$

That distinction lets us use geometry without pretending that arbitrary vector division exists.

The next two essays separate the two readings and then reunite them through the shared equation $a=bc$.
