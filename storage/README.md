# Research storage

Research owns the persistence and retrieval of the papers and notebooks it
produces.

```text
storage/
├── local/
│   ├── routes.toml         # K identity to local-file map
│   └── T-*/...             # versioned research corpus
├── google-drive/
│   └── routes.toml         # future Drive locations and replica metadata
└── storage.toml            # source registry
```

## Local

[`local/`](local/) mirrors K rooted paths. A content path omits the extension:

```text
T-math/L-division/F-01-introduction
```

[`local/routes.toml`](local/routes.toml) binds each immutable K UUID and rooted
path to a file location. Research can therefore resolve either selector to:

```text
storage/local/T-math/L-division/F-01-introduction.md
```

A local route is explicit even when `path` and `location` currently match:

```toml
[[route]]
id = "ff647a5d-44f0-42af-9f01-abcadd04fb37"
path = "T-math/L-division/F-01-introduction"
format = "md"
location = "T-math/L-division/F-01-introduction.md"
```

The UUID remains stable if K later moves the node. Updating the rooted path in
this map preserves ID-based retrieval, while storage audits can reveal a stale
path on another replica. Identity stays in the route map rather than document
front matter, so the same resolver works for Markdown, notebooks, Drive files,
and future formats without rewriting their content bodies.

The current corpus was copied from Foundations. Foundations remains the stable
legacy source used by existing consumers during the transition.

## Google Drive

[`google-drive/routes.toml`](google-drive/routes.toml) is intentionally empty.
When the Drive layout is settled, each route can record the same K UUID and
rooted path, plus its format, URI, modification time, and checksum. The CLI can
then compare local and Drive replicas without placing credentials in this
repository.

The future entry shape is deliberately small:

```toml
[[route]]
id = "ff647a5d-44f0-42af-9f01-abcadd04fb37"
path = "T-math/L-division/F-01-introduction"
format = "md"
uri = "https://drive.google.com/..."
modified_at = "2026-08-03T12:00:00Z"
sha256 = "..."
```

After routes exist, `sources.google-drive.enabled` in `storage.toml` activates
them for discovery, resolution, and replica comparison.

The storage-query interface is documented in
[`../tooling/README.md`](../tooling/README.md).
