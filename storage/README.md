# Research storage

Research owns the persistence, inventory, and availability declarations of the
papers and notebooks it produces.

```text
storage/
├── documents/
    ├── local/
    │   ├── routes.toml     # K identity to local-file map
    │   ├── companions.toml # K identity to companion-directory map
    │   └── T-*/...         # versioned research corpus
    ├── github/
    │   └── companions.toml # versioned GitHub directory locations
    └── google-drive/
        ├── routes.toml     # Drive document locations
        └── companions.toml # Drive companion-directory locations
└── projects/               # storage grouping, not a contributor domain
    ├── code/
    │   ├── local/          # self-contained executable projects
    │   └── github/         # published project locations
    └── media/
        ├── local/          # ignored reproducible renders
        └── youtube/        # published video locations
```

The root [`contributor.toml`](../contributor.toml) declares Research's domains
and stores independently, then binds them through explicit `[[bindings]]`.

The first level partitions Research-owned domains. Inside a domain, each
directory expresses one persistence alternative for the same logical
resources.

## Documents / local

[`documents/local/`](documents/local/) mirrors K rooted paths. A content path
omits the extension:

```text
T-math/L-division/F-01-introduction
```

[`documents/local/routes.toml`](documents/local/routes.toml) binds each
immutable K UUID and rooted path to a file location. Research can therefore
expose either selector with a local store descriptor. Tether then projects it
to:

```text
storage/documents/local/T-math/L-division/F-01-introduction.md
```

The logical Research resource is `(node, research, documents, md)`. The local
path above is only one replica location. The same resource may later map to a
Drive URI without changing its identity.

A local route is explicit even when `path` and `location` currently match:

```toml
[[route]]
id = "ff647a5d-44f0-42af-9f01-abcadd04fb37"
path = "T-math/L-division/F-01-introduction"
format = "md"
location = "T-math/L-division/F-01-introduction.md"
```

The UUID remains stable if K later moves the node. Updating the rooted path in
this map preserves ID-based discovery. Identity stays in the route map rather
than document front matter, so the same contributor protocol works for
Markdown, notebooks, Drive files, and future formats without rewriting their
content bodies.

The local binding uses `pattern = "{path}.{format}"`, so it mirrors K's current
grouping path. That is a Research storage decision, not a protocol
requirement. Another contributor may use `{id}.{format}` or an explicit map.

### Document companions

A `documents/companions` resource is one directory located at the same rooted
path stem as its owning K node. For the Experimental Laboratory, the Markdown
file and companion directory are siblings:

```text
F-04-experimental-laboratory.md
F-04-experimental-laboratory/
├── condition-comparison.png
├── energy-comparison.png
└── peak-structures.png
```

The Markdown references these files through the directory name. Tether can
copy the complete local companion directory with `--layout dir`. GitHub and
Drive publish mapped folder URIs; they remain useful for discovery even when a
remote folder protocol cannot be materialized as a single file download.
The `*-companions` store ids distinguish their mapped-directory protocol from
the file-oriented stores on the same physical hosts.

The current corpus was copied from Foundations. Foundations remains the stable
legacy source used by existing consumers during the transition.

## Projects / code and media

`projects/` groups reproducible studies by storage concern. It does not appear
in K's resource identity. The current patchy-particle study registers its
self-contained HOOMD-blue environment as `research/code/python-project` and
its reproducible animation as `research/media/mp4` on the same Experimental
Laboratory node.

Local and GitHub code inventories point to the complete project directory,
including its Pixi environment and rendering entry points. Local MP4 files are
ignored because they can be reproduced; their route inventory remains
versioned. YouTube is a disabled mapped store until its public URI is supplied.

## GitHub

The GitHub template reuses `documents/local/routes.toml` because the Research
repository preserves the same
`storage/documents/local/<path>.<format>` layout. The active remote is the
public `Cohesian/research` repository.

## Documents / Google Drive

[`documents/google-drive/routes.toml`](documents/google-drive/routes.toml)
records the same K UUID, rooted path, and format as the local inventory, plus
the provider-controlled URI. No credentials belong in the protocol or
inventory.

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

After routes exist, `stores.google-drive.enabled` in `contributor.toml`
activates them for discovery. Its `map` strategy lets Tether
interpret Drive-controlled URIs.

The common query interface is documented in
[Tether's README](../../tether/README.md).
