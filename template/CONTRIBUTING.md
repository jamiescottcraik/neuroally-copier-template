# Contributing to {{ project_name }}

**First off—thank you for helping make this scaffold stronger!**
We’re building *accessible, modular, and ethical AI tools* anyone can run, learn from, and extend.

---

## 🚀 Quickstart for Contributors

1. **Fork and Clone:**
   ```bash
   git clone https://github.com/{{ github_username }}/{{ project_slug }}.git
   cd {{ project_slug }}
````

2. **Install Requirements:**

   * **Poetry (recommended):**

     ```bash
     poetry install
     pre-commit install
     ```

   * Or use Conda/UV as described in the [README](README.md).

3. **Set Up Local Environment:**

   * Copy `.env.example` to `.env` and add only the keys you need.
   * **Never commit secrets**—`.env` is gitignored.

4. **Check the Basics:**

   * Run tests:

     ```bash
     poetry run pytest
     ```
   * Check lint:

     ```bash
     poetry run ruff check .
     ```
   * Check typing:

     ```bash
     poetry run mypy src/
     ```
   * Format code:

     ```bash
     poetry run black .
     ```
   * Run all checks (if you have a Makefile):

     ```bash
     make check
     ```

---

## 🗂️ Code Style

* **Formatter:** [Black](https://black.readthedocs.io/en/stable/)
* **Linter:** [Ruff](https://docs.astral.sh/ruff/)
* **Type Checking:** [Mypy](http://mypy-lang.org/)
* **Pre-commit:** Configured—run `pre-commit install` after setup.

All code **must pass formatting, linting, and typing before merging.**
*Don’t waste time fighting style—just run*

```bash
make format lint typecheck
```

---

## 📦 Project Structure

* Source code: `src/`
* Providers: `src/providers/{{ main_category }}/`
* Config/settings: `src/config/`
* Tests: `tests/`
* Docs: `docs/`

Provider logic should be modular—*never* hardcode keys or mix unrelated API logic.

---

## 🧪 Adding New Providers or Features

* **To add a provider:**

  * Create a new file in `src/providers/{{ main_category }}/` (e.g., `openai_provider.py`)
  * Follow existing examples and docstrings.
  * Update any relevant docs in `docs/`.

* **To add features or fixes:**

  * Open a new branch (`feature/my-feature`, `fix/bug-description`)
  * Write tests for new code or changes.
  * Update docs if needed.

---

## 📄 Documentation

* Docs live in `docs/` and are built with [MkDocs Material](https://squidfunk.github.io/mkdocs-material/).
* Run locally with:

  ```bash
  poetry run mkdocs serve
  ```
* For multi-version docs, see the mike plugin config.

---

## 🗝️ Security & Ethics

* No secrets, keys, or passwords in code or commit history—**ever**.
* Respect accessibility and neuro-inclusivity best practices.
* PRs violating ethical or inclusion standards will be closed—no hard feelings.

---

## 🛠️ Submitting a Pull Request

* Keep PRs focused—one topic/change per PR.
* Link related issues, if any.
* Ensure CI and all pre-commit hooks pass.
* Be open and responsive during code review.

---

## 📢 Questions or Ideas?

* Open an issue or PR.
* Tag {{ author\_name }} (\[{{ github\_username }}]\([https://github.com/{{](https://github.com/{{) github\_username }})) for a response.
* More at [NeuroAlly.AI](https://neuroally.ai/).

---

**Thanks for helping keep this project accessible, robust, and future-proof.**

