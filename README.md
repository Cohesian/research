# Cohesian Research

Research is Cohesian's workspace for developing ideas into papers, notebooks,
and related academic content.

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
│   └── documents/          # Research-owned contributor domain
│       ├── local/          # corpus plus its identity route map
│       └── google-drive/   # Drive route inventory
├── README.md
└── AGENTS.md
```

The `documents` domain contains its persistence alternatives. The local corpus
preserves the rooted K paths copied from Foundations, while the Drive map
binds the same logical resources to provider-controlled URIs. Foundations
remains unchanged while existing consumers migrate.

Research proposals to K and storage discovery are separate operations: K may
accept a research contribution, while Research remains responsible for making
the corresponding content available. The root contributor protocol exposes
Research's domains, stores, bindings, and inventories to Tether without
requiring Research-specific bridge code.

Research is contributor-ready now: its id is `research`, its domain is
`documents`, and its 25 local `md`/`ipynb` resources match K's accepted
registry. GitHub exposes the same versioned corpus as an active remote store.
Google Drive remains a disabled private backup.

## License

Software and tooling use the [MIT License](LICENSE). Papers and other research
content use [Creative Commons Attribution 4.0](LICENSE-CONTENT).
