# Cohesian Research

Research is Cohesian's workspace for developing ideas into papers, notebooks,
executable studies, and related academic content.

It may work independently or prepare TLF-compatible proposals for K. Research
owns the content it produces, the storage replicas it maintains, and the
declarations needed to discover those replicas.

## Start here

| Need | Read |
|---|---|
| Research role | [`AGENTS.md`](AGENTS.md) |
| Workspace and K relationship | [`docs/README.md`](docs/README.md) |
| Storage layout | [`storage/README.md`](storage/README.md) |
| Contributor protocol | [`contributor.toml`](contributor.toml) |
| Tether bridge | [`../tether/README.md`](../tether/README.md) |

## Repository shape

```text
research/
├── contributor.toml       # domains, stores, and their bindings
├── docs/                   # Research workspace documentation
├── storage/
│   ├── documents/          # papers and notebooks
│   │   ├── local/          # corpus plus its identity route map
│   │   └── google-drive/   # Drive route inventory
│   └── projects/           # storage grouping for executable studies
│       ├── code/           # reproducible project sources
│       └── media/          # rendered research media
├── README.md
└── AGENTS.md
```

The `documents`, `code`, and `media` domains contain distinct resource formats.
`documents/companions` represents one directory of document-owned supporting
files, allowing a paper and its figures to be materialized independently but
rejoined by their common K selector.
The local document corpus preserves K rooted paths, while explicit maps bind
project code and rendered media to the same canonical K selectors.
Foundations remains unchanged while existing consumers migrate.

Research proposals to K and storage discovery are separate operations: K may
accept a research contribution, while Research remains responsible for making
the corresponding content available. The root contributor protocol exposes
Research's domains, stores, bindings, and inventories to Tether without
requiring Research-specific bridge code.

Research is contributor-ready now: its id is `research`, and its active local
inventories cover documents, executable code, and rendered media. GitHub
exposes the versioned document and code resources. Google Drive remains a
disabled private document backup, and YouTube remains disabled until the
Physics video URI is published.

## License

Software and tooling use the [MIT License](LICENSE). Papers and other research
content use [Creative Commons Attribution 4.0](LICENSE-CONTENT).
