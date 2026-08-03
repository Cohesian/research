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
| Storage interface | [`tooling/README.md`](tooling/README.md) |
| Canonical TLF | [`../../k-graph/docs/TLF.md`](../../k-graph/docs/TLF.md) |
| Contributor contract | [`../../k-graph/docs/CONTRIBUTORS.md`](../../k-graph/docs/CONTRIBUTORS.md) |

## Working model

Research content lives under `storage/local/` at its rooted K path:

```text
storage/local/<rooted-path>.<format>
```

Every stored object is addressed by K's immutable UUID, its current rooted
path, or both. `storage/local/routes.toml` binds those selectors to local
files. Google Drive locations will use the same identity pair in
`storage/google-drive/routes.toml` after that layout is chosen. The source
registry is `storage/storage.toml`; credentials remain in the owning
environment.

There is no repository-wide writing template yet. Let the question, intended
reader, and task instructions determine the form of each paper.

## Validation

From the repository root:

```bash
PYTHONPATH=tooling PYTHONDONTWRITEBYTECODE=1 \
  python -m unittest discover -s tooling/tests
PYTHONPATH=tooling PYTHONDONTWRITEBYTECODE=1 \
  python -m research_storage.cli storages
git diff --check
```
