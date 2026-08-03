# Research workspace

Research develops ideas into academic papers, notebooks, and related content.
An idea may come from a person, from K, or from work already happening inside
Research.

Research can produce one File, several Files, a Lecture-sized collection, or a
small Topic-shaped collection. The writing process itself is independent of K.
When Research wants that work represented in the accepted graph, it prepares a
proposal matching K's TLF domain.

The canonical contracts live in [`Cohesian/k-graph`](../../../k-graph/):

- [`docs/TLF.md`](../../../k-graph/docs/TLF.md)
- [`docs/CONTRIBUTORS.md`](../../../k-graph/docs/CONTRIBUTORS.md)
- [`docs/PROPOSALS.md`](../../../k-graph/docs/PROPOSALS.md)

K owns accepted knowledge identity and topology. Research owns its papers,
notebooks, replicas, and retrieval interface. Each accepted K node has two
selectors: an immutable UUID and a rooted path that may change when grouping
topology changes. Research records both, so callers can resolve content by
either selector and detect stale path mappings across replicas.

Storage is described in [`../storage/README.md`](../storage/README.md), and the
query interface in [`../tooling/README.md`](../tooling/README.md).
