# Research workspace

Research develops scientific content. A result may be one paper, a notebook,
a small TLF subgraph, an executable experiment, a video, or a composition of
several of those resources.

The research process is independent of K. Registration begins only when a
result is proposed for the accepted graph.

## Boundary with K

K owns accepted node identity and topology. Research owns resource bytes,
replicas, and publications. Their stable join is

$$
(\operatorname{id}(v),\,c,\,H,\,p)
\longmapsto (q,z),
$$

where $c=\text{research}$, $H$ is the hierarchy, $p$ is the resource key,
$q$ is its protocol, and $z$ is the protocol-defined SHA-256.

The rooted K path is retained as a readable, checked selector. It may change
after a grouping rewrite; the node UUID and resource address remain stable.

Research's active hierarchies are `documents`, `code`, and `media`. Resource
protocols describe the boundary independently from file extension:

- `markdown-file@1` is one Markdown file;
- `markdown-bundle@1` is a Markdown entrypoint plus its same-stem assets;
- `jupyter-notebook-file@1` is one notebook source;
- `python-project@1` is a bounded reproducible project; and
- `mp4-file@1` is one exact video file.

Studio produces media without becoming its owner in K. After delivery,
Research stores the source project and/or video, computes their digests, and
records Studio only as optional provenance. The current binder scene projects
and videos follow this flow.

The canonical specifications live in
[`Cohesian/k-graph`](../../k-graph/docs/RESOURCE-CONTRACT-V2.md) and
[`Cohesian/tether`](../../tether/docs/CONTRIBUTOR-PROTOCOL-V2.md).
