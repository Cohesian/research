# Research storage

Research owns the persistence and availability declarations of its scientific
resources. Protocol v2 keeps one flat inventory for each semantic hierarchy:

```text
storage/
├── documents/
│   ├── resources.toml
│   ├── local/
│   ├── google-drive/
│   └── github/
└── projects/
    ├── code/
    │   ├── resources.toml
    │   ├── local/
    │   └── github/
    └── media/
        ├── resources.toml
        ├── local/
        └── youtube/
```

The directory tree is a physical storage choice. It is not a copy of K's
topology contract. Each `resources.toml` record carries both the immutable K
UUID and the current rooted path, so Tether can query either representation.

## Resource-local locations

A v2 record keeps every replica beside the resource it describes:

```toml
[[resource]]
node_id = "..."
path = "T-physics/.../F-04-experimental-laboratory"
key = "emergence-video"
protocol = "mp4-file@1"
sha256 = "..."
locations = [
  { store = "local", relation = "exact", location = "storage/projects/media/local/.../emergence.mp4" },
  { store = "youtube", relation = "publication", uri = "https://youtu.be/..." },
]
```

An `exact` location must reproduce the declared SHA under its protocol. A
`publication` may be transformed by its host and remains useful for embedding,
but it does not claim byte equality.

## Documents

Most Markdown entries use `markdown-file@1`. The Experimental Laboratory uses
`markdown-bundle@1`: its `.md` entrypoint and same-stem image directory form
one canonical resource. Its local location is exact. GitHub file URLs are
declared for single-file documents and notebooks; a multi-file GitHub transfer
adapter can later expose the bundle as a remote exact location.

Google Drive remains a disabled backup store. Its v1 route map is retained as
transition data but is not part of the active v2 inventory.

## Code and media

The HOOMD study is a `python-project@1` resource. Its Pixi environment and
runtime outputs are outside the canonical project boundary; `pixi.toml` and
`pixi.lock` preserve the executable environment declaration.

The rendered emergence video is exact in local storage and a publication on
YouTube. Local MP4 bytes remain ignored by Git while their digest and route are
versioned in `storage/projects/media/resources.toml`.

Future Studio deliveries can enter these inventories with
`produced_by = "studio"`. Research remains the contributor and storage owner.
