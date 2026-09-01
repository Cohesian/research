# Research workspace

Research develops ideas into academic papers, notebooks, and related content.
An idea may come from a person, from K, or from work already happening inside
Research.

Research can produce one File, several Files, a Lecture-sized collection, or a
small Topic-shaped collection. A study may combine prose, a notebook, an
executable project, and rendered media. The research process itself is
independent of K. When Research wants that work represented in the accepted
graph, it prepares a proposal matching K's TLF and resource domains.

The canonical contracts live in [`Cohesian/k-graph`](../../../k-graph/):

- [`docs/TLF.md`](../../../k-graph/docs/TLF.md)
- [`docs/CONTRIBUTORS.md`](../../../k-graph/docs/CONTRIBUTORS.md)
- [`docs/PROPOSALS.md`](../../../k-graph/docs/PROPOSALS.md)

K owns accepted knowledge identity and topology. Research owns its papers,
notebooks, replicas, and contributor protocol. Each accepted K node has two
selectors: an immutable UUID and a rooted path that may change when grouping
topology changes. Research records both, so Tether can discover
content by either selector.

Research exposes three contributor domains: `documents`, `code`, and `media`.
One Research resource is uniquely identified by
`(K node, research, domain, format)`. It has no separate resource name:
`md`, `ipynb`, `companions`, `python-project`, and `mp4` are distinct resource
leaves, while a second store represents a replica rather than another
resource. A `companions` leaf is a directory bundle for files referenced by a
document; it is not another paper and does not require identities for each
contained file.

Storage is described in [`../storage/README.md`](../storage/README.md). The
localized bridge is [`../contributor.toml`](../contributor.toml); its common
protocol is implemented by [Tether](../../tether/).
The contributor identity and resource-registration steps are summarized in
[Tether's onboarding guide](../../tether/docs/CONTRIBUTOR-ONBOARDING.md).
