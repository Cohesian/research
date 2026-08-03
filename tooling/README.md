# Research storage tooling

This Python project exposes Research-owned storage discovery and resolution.
It does not connect to K or write across repositories.

## Install

From the Research repository root:

```bash
python3 -m venv .venv
.venv/bin/python -m pip install -e ./tooling
```

## Discover storages

```bash
.venv/bin/research-storage storages
```

## Discover content

By immutable K UUID:

```bash
.venv/bin/research-storage list \
  --id ff647a5d-44f0-42af-9f01-abcadd04fb37
```

Or by the current rooted path:

```bash
.venv/bin/research-storage list \
  --path T-math/L-division/F-01-introduction
```

## Resolve a URI

```bash
.venv/bin/research-storage resolve \
  --id ff647a5d-44f0-42af-9f01-abcadd04fb37 \
  --format md \
  --source local
```

Commands accept `--id`, `--path`, or both. Passing both asks for the route that
matches the complete identity pair.

## Compare replicas

```bash
.venv/bin/research-storage status \
  --path T-math/L-division/F-01-introduction \
  --format md \
  --json
```

`status` compares checksums when each replica declares one, checks whether all
replicas agree on the current rooted path, and reports the source with the
latest declared modification time. A single replica is available but has no
cross-storage synchronization state.

Audit every known content object:

```bash
.venv/bin/research-storage audit --json
```

The summary separates synchronized replicas, content drift, path drift,
single-source content, unavailable routes, and multi-source content whose
checksums are not known.

## Tests

```bash
PYTHONPATH=tooling PYTHONDONTWRITEBYTECODE=1 \
  python -m unittest discover -s tooling/tests
```
