# Cohesian Research — agent guidance

## Purpose

Act as a Research collaborator. Develop ideas into papers, notebooks,
executable studies, explanations, derivations, and scientific media.

Research work may begin independently or from an existing K node. When it is
proposed to K, express the topology and resource overlay according to the
canonical contracts in [`../k-graph/`](../k-graph/).

## Read first

| Need | Read |
|---|---|
| Workspace overview | [`README.md`](README.md) |
| Research and K | [`docs/README.md`](docs/README.md) |
| Storage ownership | [`storage/README.md`](storage/README.md) |
| Contributor package | [`contributor.toml`](contributor.toml) |
| Resource contract v2 | [`../k-graph/docs/RESOURCE-CONTRACT-V2.md`](../k-graph/docs/RESOURCE-CONTRACT-V2.md) |
| Tether protocol v2 | [`../tether/docs/CONTRIBUTOR-PROTOCOL-V2.md`](../tether/docs/CONTRIBUTOR-PROTOCOL-V2.md) |
| Canonical TLE | [`../k-graph/docs/TLE.md`](../k-graph/docs/TLE.md) |

## Working model

Research owns three active hierarchy inventories:

```text
documents
code
media
```

Each inventory record binds a K node UUID, an optional current rooted path,
and a local resource key to one versioned protocol and canonical SHA-256. Its
`locations` list describes the exact replicas or publications Research
currently exposes.

Use `markdown-bundle@1` when a Markdown entrypoint has a same-stem asset
directory. Use `markdown-file@1` when the Markdown file is the complete
resource. Notebooks, MP4 files, and Python projects use their corresponding
protocols from Tether's registry.

Studio is a production workstation. When it produces accepted scientific
media or a Loci project for Research, Research stores and registers that
resource; `produced_by = "studio"` records provenance when useful.

## Updating a resource

After changing resource bytes, recalculate the digest with Tether and update
the matching `resources.toml` record. The same protocol and digest are later
copied into K's accepted overlay.

```bash
PYTHONPATH=../tether python -m tether.cli resource digest \
  storage/documents/local/path/to/paper.md \
  --protocol markdown-file@1
```

## Validation

From the repository root:

```bash
PYTHONPATH=../tether PYTHONDONTWRITEBYTECODE=1 \
  python -m tether.cli contributor check .
PYTHONPATH=../tether PYTHONDONTWRITEBYTECODE=1 \
  python -m tether.cli resource list . --hierarchy documents
git diff --check
```
