# Linear Algebra Topic Proposal

## Purpose

Develop a connected path from scalar coefficients to vectors, linear transformations, matrices, and tensors while preserving the existing Linear Algebra and Vectors topology.

Research proposes the content below. K-graph remains responsible for assigning identifiers to new nodes and accepting the final topology.

## Proposed TLE

```text
T-linear-algebra                                  existing
├── L-foundations                                new
│   ├── E-01-scalars-and-fields
│   ├── E-02-vector-spaces
│   └── E-03-linear-combinations
├── T-vectors                                    existing
│   ├── L-vector-operations                      new
│   │   ├── E-01-addition-and-subtraction
│   │   ├── E-02-scalar-multiplication
│   │   ├── E-03-magnitude-direction-and-dot-product
│   │   └── E-04-vector-laboratory.ipynb
│   ├── L-basis                                  existing
│   │   ├── E-01-introduction                    existing, rewritten
│   │   └── E-02-basis-laboratory.ipynb
│   └── L-reflection                             existing
│       ├── E-01-introduction                    existing, rewritten
│       ├── E-02-constructing-the-matrix
│       ├── E-03-eigendirections-and-invariants
│       └── E-04-reflection-laboratory.ipynb
├── L-linear-transformations                     new
│   ├── E-01-transforming-a-basis
│   ├── E-02-matrices-as-linear-maps
│   ├── E-03-two-views-of-matrix-multiplication
│   ├── E-04-image-kernel-and-rank
│   └── E-05-transformation-laboratory.ipynb
└── L-tensors                                    new
    ├── E-01-from-linear-to-multilinear
    ├── E-02-components-order-and-shape
    ├── E-03-basis-independent-objects
    └── E-04-tensor-laboratory.ipynb
```

## Existing canonical identities

- `T-linear-algebra`: `37988c21-5843-4b3e-84ac-e80b338f0322`
- `T-vectors`: `ae514a05-eb83-4013-a8c9-b1aaab27100b`
- `L-basis`: `47a4d65e-41fe-4026-b87c-11050d29bacd`
- `L-basis/E-01-introduction`: `edba87bc-3359-4ea1-bfb7-7bb5d4762963`
- `L-reflection`: `2a9874d9-5c7e-414f-8959-1364f177aa84`
- `L-reflection/E-01-introduction`: `07ff1a0b-e84f-40bb-996f-467a03d2bf3c`

K-graph assigned the remaining identifiers during acceptance:

- `L-foundations`: `f1f661bc-4e84-44b6-bc46-ca3706bef35c`
- `L-foundations/E-01-scalars-and-fields`: `f379e3eb-b603-4d86-829d-aafe5f5466ff`
- `L-foundations/E-02-vector-spaces`: `34255a7e-13f8-462e-a1b8-fee604de8893`
- `L-foundations/E-03-linear-combinations`: `598dd717-aaa4-42ed-bbb1-6ca7e1075209`
- `L-vector-operations`: `20749194-7a1d-47e0-b4d7-e954e01c9db8`
- `L-vector-operations/E-01-addition-and-subtraction`: `13ac5aa2-9e33-4875-a3b9-5f1a86f9171b`
- `L-vector-operations/E-02-scalar-multiplication`: `183d90f0-8306-4b96-adef-88c2bc842d07`
- `L-vector-operations/E-03-magnitude-direction-and-dot-product`: `b5dfbb83-1557-4359-8a96-8a5b05d98d23`
- `L-vector-operations/E-04-vector-laboratory`: `0fc19d85-98e6-4def-a55a-121ce4a43140`
- `L-basis/E-02-basis-laboratory`: `b43ad2ae-5d94-41f8-9c15-2bc47044cdeb`
- `L-reflection/E-02-constructing-the-matrix`: `d7056ff7-6fd2-46c7-aa19-783694a41739`
- `L-reflection/E-03-eigendirections-and-invariants`: `5387742c-e801-4f99-92a1-3ebdb67235d3`
- `L-reflection/E-04-reflection-laboratory`: `3cfa86df-e1aa-4b78-9b77-6925a72eff67`
- `L-linear-transformations`: `d4de6f3a-f2d6-405e-a9c2-5f97926a9d50`
- `L-linear-transformations/E-01-transforming-a-basis`: `09562bd6-0337-4d1b-94ec-1d6b43694841`
- `L-linear-transformations/E-02-matrices-as-linear-maps`: `72f5419c-8895-4d86-abbf-40374e67a3e8`
- `L-linear-transformations/E-03-two-views-of-matrix-multiplication`: `89b5e274-1438-45b7-a799-998d4fab0dfd`
- `L-linear-transformations/E-04-image-kernel-and-rank`: `9f55051c-9669-4a78-92b4-9e20b885c1bd`
- `L-linear-transformations/E-05-transformation-laboratory`: `99a067c0-f590-4e61-9390-88170fbb4fb6`
- `L-tensors`: `bf53e733-356a-41ee-962b-3f0a523ace7d`
- `L-tensors/E-01-from-linear-to-multilinear`: `63ed346b-8aa1-418d-8b92-6f10e5d74dc6`
- `L-tensors/E-02-components-order-and-shape`: `77ce02d1-567f-4704-b099-76d1391b80e4`
- `L-tensors/E-03-basis-independent-objects`: `b04ed194-a816-42e5-b950-ab46846cbf41`
- `L-tensors/E-04-tensor-laboratory`: `64d860f7-3329-4311-96a5-67a5da67a5c0`

## Pedagogical order

At the top level, propose the linear sequence:

```text
L-foundations
  -> T-vectors
  -> L-linear-transformations
  -> L-tensors
```

Inside `T-vectors`, propose:

```text
L-vector-operations -> L-basis -> L-reflection
```

Within each new lecture, the listed essays form a `NEXT` chain in filename order.

## Proposed resources

Every prose essay uses `md` with `markdown-file@1`. Every visual laboratory uses `ipynb` with `jupyter-notebook-file@1`.

The existing Basis and Reflection introductions retain their current paths and identifiers, but their content and accepted SHA values should be updated.

## Mathematical boundaries

- Scalars are elements of a field; physical meaning and units come from context.
- Magnitude and geometric direction require additional structure such as a norm or inner product; they are not intrinsic to every abstract vector space.
- For an $m\times n$ matrix, columns lie in the $m$-dimensional codomain and inputs have $n$ coordinates.
- Matrix-vector multiplication is simultaneously a linear combination of columns and a collection of row-vector dot products.
- A reflection preserves its mirror eigenspace, reverses the normal eigenspace, and has matrix $R=2\vec u\vec u^{\mathsf T}-I$ for a unit mirror direction $\vec u$.
- A tensor is not defined merely as a multidimensional array. Arrays are coordinate representations of multilinear, basis-independent objects.
