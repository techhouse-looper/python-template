# python-template 🐍

A small Python starter with strict defaults, fast feedback, and a package layout that scales past
the first weekend.

The goal is simple: start from a clean baseline, keep the toolchain boring, and make quality checks
cheap enough to run all the time.

## Defaults

- `uv` for dependency and lockfile management
- `src/` layout with Hatchling packaging
- Click for a minimal CLI entry point
- Ruff, Pyright, and pytest as the default quality bar
- GitHub Actions for CI, build validation, and release artifacts

## Quickstart

```bash
make setup-dev
make check
uv run python -m python_template --help
uv run python -m python_template hello
```

Sample output:

```text
Let's build something fun, Yujeong.
```

## Core commands

| Command | Purpose |
| --- | --- |
| `make setup` | Install runtime dependencies |
| `make setup-dev` | Install runtime and development dependencies |
| `make format` | Format the codebase with Ruff |
| `make lint` | Run Ruff lint checks |
| `make lint-fix` | Run Ruff and apply safe fixes |
| `make typecheck` | Run Pyright in strict mode |
| `make test` | Run pytest |
| `make test-cov` | Run pytest with coverage |
| `make check` | Run format, lint, typecheck, and tests |
| `make build` | Build the wheel and sdist |
| `make lock` | Refresh `uv.lock` without upgrading |
| `make update` | Upgrade dependencies and refresh `uv.lock` |

## Project layout

```text
.
├── .github/workflows/
├── src/python_template/
├── tests/
├── .pre-commit-config.yaml
├── Makefile
├── pyproject.toml
└── uv.lock
```

## Quality defaults

This template is intentionally strict by default:

- **Ruff** enforces formatting, imports, docstrings, naming, typing hygiene, and common bug-prone
  patterns.
- **Pyright** runs in `strict` mode.
- **pytest** is the default regression layer.

If a real project constraint justifies relaxing a rule, change it deliberately. The default posture
is to keep the baseline tight.

## GitHub Actions

The repository ships with three focused workflows:

- `ci.yml` — lint, typecheck, and test on Python 3.11–3.13
- `build.yml` — build the package and smoke-test the generated wheel
- `release.yml` — build and upload release artifacts for version tags

## License

MIT.
