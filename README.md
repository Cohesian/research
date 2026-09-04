# Cohesian Research

Research is Cohesian's workspace and contributor for papers, notebooks,
executable studies, and scientific media. It may develop work independently;
accepted resources are attached to K nodes through the contributor contract.

## Start here

| Need | Read |
|---|---|
| Research role | [`AGENTS.md`](AGENTS.md) |
| Relationship with K | [`docs/README.md`](docs/README.md) |
| Resource persistence | [`storage/README.md`](storage/README.md) |
| Machine-readable package | [`contributor.toml`](contributor.toml) |
| Shared bridge | [`../tether/README.md`](../tether/README.md) |

## Resource model

Research implements contributor protocol v2. One resource address is

$$
(\operatorname{id}(v),\,\text{research},\,H,\,p),
$$

where $H$ is an arbitrary hierarchy and $p$ is a resource key local to that
K node and hierarchy. The current inventories are:

- `documents`: Markdown files, Markdown bundles, and Jupyter notebooks;
- `code`: reproducible source projects; and
- `media`: reproducible scene projects and rendered scientific media.

Every resource declares its protocol, canonical SHA-256, and its own available
locations. Research owns those bytes and locations. K owns accepted identity,
topology, protocol, and digest. Tether validates and joins both descriptions.

Studio produces the current K-linked Loci projects and binder videos on
Research's behalf. Those records remain owned by `research` and carry
`produced_by = "studio"` as provenance; that field does not alter their
logical address.

## Repository shape

```text
research/
├── contributor.toml
├── docs/
├── storage/
│   ├── documents/
│   │   ├── resources.toml
│   │   └── local/
│   └── projects/
│       ├── code/resources.toml
│       └── media/resources.toml
├── README.md
└── AGENTS.md
```

The older `routes.toml` files remain as transition references for protocol v1.
`contributor.toml` and the three `resources.toml` inventories are the active v2
package.

## Validation

```bash
PYTHONPATH=../tether python -m tether.cli contributor check .
PYTHONPATH=../tether python -m tether.cli resource list .
```

## License

Software and tooling use the [MIT License](LICENSE). Papers and other research
content use [Creative Commons Attribution 4.0](LICENSE-CONTENT).
