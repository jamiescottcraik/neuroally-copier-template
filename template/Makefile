# Makefile for {{ project_name }} — dev, test, docs, and env management

.PHONY: help install test lint format typecheck docs build-docs clean env export-env check update

help:  ## Show this help
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-18s\033[0m %s\n", $$1, $$2}'

install:  ## Install all dependencies via Poetry
	poetry install

test:  ## Run all tests with pytest
	poetry run pytest

lint:  ## Run Ruff linter
	poetry run ruff check .

format:  ## Run Black code formatter
	poetry run black .

typecheck:  ## Run mypy static type checker
	poetry run mypy src/

docs:  ## Serve documentation locally with MkDocs
	poetry run mkdocs serve

build-docs:  ## Build documentation site
	poetry run mkdocs build

clean:  ## Remove build, test, and Python cache files, including .venv if present
	find . -type d -name "__pycache__" -exec rm -rf {} +
	find . -type d -name ".pytest_cache" -exec rm -rf {} +
	find . -type d -name ".venv" -exec rm -rf {} +
	rm -rf .mypy_cache .ruff_cache .pytest_cache .coverage htmlcov dist build site

env:  ## Show current Poetry environment info
	poetry env info

export-env:  ## Export requirements and environment.yml for Conda/UV
	poetry export -f requirements.txt --output requirements.txt --without-hashes
	poetry export -f requirements.txt --output requirements-dev.txt --dev --without-hashes
	conda env export > environment.yml

check: lint format typecheck test  ## Run all checks (lint, format, type, tests)

update:  ## Update dependencies to latest allowed versions
	poetry update
