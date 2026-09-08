# Calculus Topic Proposal

## Purpose

Introduce differential and integral calculus through one continuous example:

$$
f(x)=x^2.
$$

The proposed lecture begins with observable finite changes, removes the measuring scale through a limit, interprets the derivative as a field of local rules, and reconstructs macroscopic change through integration.

Research proposes the content and topology below. K-graph remains responsible for assigning canonical identifiers and accepting the topology into the registry.

## Proposed TLE

```text
T-calculus
└── L-local-change-and-accumulation
    ├── E-01-finite-change
    ├── E-02-the-derivative
    ├── E-03-a-field-of-local-rules
    ├── E-04-reconstruction-by-integration
    └── E-05-visual-laboratory
```

All nodes in this proposal are new. K-graph should assign their canonical identifiers during acceptance.

## Proposed grouping edges

- `T-math` groups `T-calculus`.
- `T-calculus` groups `L-local-change-and-accumulation`.
- `L-local-change-and-accumulation` groups each proposed essay.

## Proposed linear edges

```text
E-01-finite-change
  -> E-02-the-derivative
  -> E-03-a-field-of-local-rules
  -> E-04-reconstruction-by-integration
  -> E-05-visual-laboratory
```

Each arrow proposes one `NEXT` edge. The corresponding inverse can be exposed as `PREV` according to the K-graph convention.

No related edges are required in the first version.

## Proposed resources

| Node | Resource key | Protocol |
| --- | --- | --- |
| `E-01-finite-change` | `md` | `markdown-file@1` |
| `E-02-the-derivative` | `md` | `markdown-file@1` |
| `E-03-a-field-of-local-rules` | `md` | `markdown-file@1` |
| `E-04-reconstruction-by-integration` | `md` | `markdown-file@1` |
| `E-05-visual-laboratory` | `ipynb` | `jupyter-notebook-file@1` |

The notebook is a static, executed resource whose implementation cells may be hidden by consumers.

## Mathematical invariants

- The finite difference uses $h\neq0$.
- The derivative uses a limit; it does not assume a smallest positive real increment.
- A slope is a rate $\Delta y/\Delta x$, while an accumulated change multiplies a local rate by a width before summation.
- The identity $f(b)-f(a)=\int_a^b f'(x)\,dx$ is used only after the relevant differentiability and continuity assumptions have been stated.
- Every numerical example is derived from $f(x)=x^2$ and is consistent with the exact expansion $(x+h)^2=x^2+2xh+h^2$.
