# Division Lecture Proposal

## Purpose

Replace the current division placeholder with a compact lecture that distinguishes the two semantic readings of division, connects them through multiplication, and gives special attention to quotients smaller than one.

Research proposes the content and topology below. K-graph remains responsible for assigning canonical identifiers to new nodes and accepting the topology into the registry.

## Proposed TLE

```text
L-division
├── E-01-introduction
├── E-02-partitive-division
├── E-03-quotative-division
├── E-04-when-the-dividend-is-smaller
└── E-05-visual-laboratory
```

The existing lecture and introduction retain their current canonical identifiers:

- `L-division`: `2c3cfe88-3010-4730-87b9-31138b863178`
- `E-01-introduction`: `ff647a5d-44f0-42af-9f01-abcadd04fb37`

K-graph assigned the remaining identifiers during acceptance:

- `E-02-partitive-division`: `3ea2de18-a6b8-4405-a6cc-bdd0a7c60c79`
- `E-03-quotative-division`: `6b3348d3-725d-4e9b-bb3e-3fe21f810661`
- `E-04-when-the-dividend-is-smaller`: `edd9880d-7aa9-4d32-a10d-4e71f04dd23b`
- `E-05-visual-laboratory`: `78460d28-94cd-4367-b8aa-8b2ea49d9330`

## Proposed grouping edges

Add one `GROUPS` edge from `L-division` to each essay in the proposed lecture.

## Proposed linear edges

```text
E-01-introduction
  -> E-02-partitive-division
  -> E-03-quotative-division
  -> E-04-when-the-dividend-is-smaller
  -> E-05-visual-laboratory
```

Each arrow proposes one `NEXT` edge. The corresponding inverse can be exposed as `PREV` according to the K-graph linear-edge convention.

No new related edges are proposed in this first version.

## Proposed resources

| Node | Resource key | Protocol |
| --- | --- | --- |
| `E-01-introduction` | `md` | `markdown-file@1` |
| `E-02-partitive-division` | `md` | `markdown-file@1` |
| `E-03-quotative-division` | `md` | `markdown-file@1` |
| `E-04-when-the-dividend-is-smaller` | `md` | `markdown-file@1` |
| `E-05-visual-laboratory` | `ipynb` | `jupyter-notebook-file@1` |

The notebook is a static visual laboratory. It should preserve its executed outputs while allowing consumers such as Site to hide implementation cells.

## Semantic invariants

- $b\neq0$ whenever $a/b$ is used.
- Both readings reconstruct the total through $a=bc$.
- Partitive division treats $b$ as a dimensionless number of equal parts.
- Quotative division compares $a$ with a unit $b$ of the same physical dimension.
- Vector diagrams represent magnitudes or scalar multiplication; the lecture does not define arbitrary vector division.
- Splitting a segment into $b$ equal pieces uses $b-1$ interior cuts.
