# Cohesian Research — agent guidance

## Purpose

Act as a Research collaborator. Develop shallow or mature ideas into papers,
notebooks, explanations, derivations, and supporting research sources.

Research work may begin independently or from an existing K node. When the
result is proposed to K, shape the proposed graph change according to the
canonical TLF and contributor contracts in [`../../k-graph/`](../../k-graph/).

## Read first

| Need | Read |
|---|---|
| Workspace overview | [`README.md`](README.md) |
| Research and K | [`docs/README.md`](docs/README.md) |
| Storage ownership | [`storage/README.md`](storage/README.md) |
| Contributor protocol | [`contributor.toml`](contributor.toml) |
| Common URI contract | [`../../../Organization/CONTRIBUTOR-STORE-RESOLUTION.md`](../../../Organization/CONTRIBUTOR-STORE-RESOLUTION.md) |
| Tether bridge | [`../tether/README.md`](../tether/README.md) |
| Canonical TLF | [`../../k-graph/docs/TLF.md`](../../k-graph/docs/TLF.md) |
| Contributor contract | [`../../k-graph/docs/CONTRIBUTORS.md`](../../k-graph/docs/CONTRIBUTORS.md) |

## Working model

Research content lives under `storage/documents/local/` at its rooted K path:

```text
storage/documents/local/<rooted-path>.<format>
```

Every stored object is addressed by K's immutable UUID, its current rooted
path, or both. `storage/documents/local/routes.toml` binds those selectors to local
files. Google Drive locations will use the same identity pair in
`storage/documents/google-drive/routes.toml`. Domains,
stores, and their many-to-many bindings are declared in `contributor.toml`;
credentials remain in the owning environment.

There is no repository-wide writing template yet. Let the question, intended
reader, and task instructions determine the form of each paper.

## Validation

From the repository root:

```bash
PYTHONPATH=../tether PYTHONDONTWRITEBYTECODE=1 \
  python -m tether.cli contributor check .
PYTHONPATH=../tether PYTHONDONTWRITEBYTECODE=1 \
  python -m tether.cli resource list . \
    --domain documents
git diff --check
```
