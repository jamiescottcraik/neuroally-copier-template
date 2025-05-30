# Changelog

All notable changes to this project will be documented in this file.

## [Unreleased]
- Add new features here before the next release.

---

## [v0.2.0] - 2025-05-29
### Added
- Pre-commit hooks: Black, Ruff, isort, mypy, nbstripout, markdownlint, yamllint.
- `.editorconfig`, `.gitignore`, `.pre-commit-config.yaml`, `.ruff.toml`, `mypy.ini`, and template configs for all tools.
- Main project scaffold: `src/`, tests, providers, and visualization modules.
- Automated CLI and plotting config in `main.py`.

### Changed
- Improved plot error handling and save/display logic.
- Tuned provider imports and config management for better extensibility.

### Removed
- Removed `*.lock` from `.gitignore` to allow `poetry.lock` commits.

### Fixed
- Sample bug fixes in plotting and config template files.

---

## [v0.1.0] - 2025-05-20
### Added
- Project initialization with Cookiecutter/Copier template.
- Core AI/data structure for `src/` and `tests/`.

---

## [0.0.1] - 2025-05-18
### Added
- First commit: project skeleton, initial README, and scaffolding files.

---

