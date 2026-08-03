# Cohesian Research

Research is Cohesian's workspace for developing ideas into papers, notebooks,
and related academic content.

It may work independently or prepare TLF-compatible proposals for K. Research
owns the content it produces, the storage replicas it maintains, and the
interface used to retrieve them.

## Start here

| Need | Read |
|---|---|
| Research role | [`AGENTS.md`](AGENTS.md) |
| Workspace and K relationship | [`docs/README.md`](docs/README.md) |
| Storage layout | [`storage/README.md`](storage/README.md) |
| Storage CLI | [`tooling/README.md`](tooling/README.md) |

## Repository shape

```text
research/
├── docs/                   # Research workspace documentation
├── storage/
│   ├── local/              # corpus plus its identity route map
│   ├── google-drive/       # future Drive route inventory
│   └── storage.toml        # source registry
├── tooling/                # Python storage discovery and resolution CLI
├── README.md
└── AGENTS.md
```

The local corpus preserves the rooted K paths copied from Foundations. Its
route map binds each immutable K UUID and current rooted path to the stored
file. Foundations remains unchanged while existing consumers migrate.

Research proposals to K and storage retrieval are separate operations: K may
accept a research contribution, while Research remains responsible for making
the corresponding content available.

## License

Software and tooling use the [MIT License](LICENSE). Papers and other research
content use [Creative Commons Attribution 4.0](LICENSE-CONTENT).
