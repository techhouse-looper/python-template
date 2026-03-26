PACKAGE ?= python_template
SRC_DIRS := src tests

.PHONY: help setup setup-dev lock update format format-check lint lint-fix typecheck test test-cov check build clean

.DEFAULT_GOAL := help

help: ## Show available tasks
	@awk 'BEGIN {FS = ":.*##"; printf "\nAvailable tasks:\n\n"} /^[a-zA-Z0-9_.-]+:.*##/ {printf "  %-20s %s\n", $$1, $$2} END {print ""}' $(MAKEFILE_LIST)

setup: ## Install the base project environment
	uv sync

setup-dev: ## Install developer dependencies
	uv sync --group dev

lock: ## Refresh uv.lock without upgrading pinned packages
	uv lock

update: ## Upgrade dependencies and refresh uv.lock
	uv lock --upgrade

format: ## Format the codebase with Ruff
	uv run ruff format $(SRC_DIRS)

format-check: ## Check formatting without modifying files
	uv run ruff format --check $(SRC_DIRS)

lint: ## Run Ruff lint checks
	uv run ruff check $(SRC_DIRS)

lint-fix: ## Run Ruff lint checks and apply safe fixes
	uv run ruff check --fix $(SRC_DIRS)

typecheck: ## Run Pyright type checking
	uv run pyright

test: ## Run tests
	PYTEST_DISABLE_PLUGIN_AUTOLOAD=1 uv run pytest

test-cov: ## Run tests with coverage
	PYTEST_DISABLE_PLUGIN_AUTOLOAD=1 uv run pytest --cov=$(PACKAGE) --cov-report=term-missing

check: format-check lint typecheck test ## Run the full local quality gate

build: ## Build wheel and sdist artifacts
	uv build

clean: ## Remove local build and tool caches
	rm -rf .venv .pytest_cache .pyright .ruff_cache .mypy_cache build dist htmlcov .coverage .coverage.*
	find . -type d -name '__pycache__' -prune -exec rm -rf {} +
