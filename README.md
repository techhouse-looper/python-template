# python-template

A minimal Python template with strict defaults for projects that want to stay small, typed, and
easy to maintain.

## What this template includes

- `uv` for dependency and lockfile management
- `src/` layout with Hatchling-based packaging
- Click-powered CLI entry point
- Ruff, Pyright, and pytest configured as the default quality bar
- GitHub Actions for CI, build validation, and tag-based release artifacts

## Quickstart

```bash
uv sync --group dev
make check
python -m python_template --help
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

This template is intentionally strict:

- **Ruff** enforces formatting, imports, docstrings, naming, typing hygiene, and common bug-prone
  patterns.
- **Pyright** runs in `strict` mode.
- **pytest** is the default regression layer.

The goal is to start from a clean baseline and relax rules only when a real project constraint
demands it.

## GitHub Actions

The repository ships with three small workflows:

- `ci.yml` — lint, typecheck, and test on Python 3.11–3.13
- `build.yml` — build the package and smoke-test the generated wheel
- `release.yml` — build and upload release artifacts for version tags

## License

MIT.
