# {{ project_name }}

Welcome to the official documentation for **{{ project_name }}**.

---

## 🚀 Overview

{{ project_name }} is a Python project template built for modern AI and ML workflows:
- **Modern Python ({{ python_version }})**
- **Pydantic, Poetry, Ruff, Black, Mypy** setup
- **Supports Conda, Poetry, and UV for flexible environments**
- **Ready for OpenAI, Gemini, Vertex, and more**
- **Full CI/CD, Docker, and documentation automation**
- **Clean onboarding and contributor experience**

---

## ⚡ Getting Started

### 1. Install Copier

[Copier](https://copier.readthedocs.io/) is the recommended way to generate a new project from this template.

```bash
pip install copier
````

### 2. Generate Your Project

```bash
copier copy gh:your-org/{{ project_slug }} your-new-project
cd your-new-project
```

* Replace `your-org` and `{{ project_slug }}` with the correct repo path.
* Copier will walk you through the template setup with prompts.

---

## 🛠️ Local Setup

Choose your preferred environment:

### Poetry (default)

```bash
poetry install
```

### Conda

```bash
conda env create -f environment.yml
conda activate {{ project_slug }}
poetry install
```

### UV (requirements.txt)

```bash
pip install uv
uv pip install -r requirements.txt
```

---

## 🧪 Preview Documentation

```bash
poetry run mkdocs serve
# or, if not using Poetry:
mkdocs serve
```

---

## 🗂️ Project Structure

```text
.
├── src/
├── docs/
├── .github/
├── pyproject.toml
├── mkdocs.yml
├── environment.yml
├── requirements.txt
├── CONTRIBUTING.md
└── ...
```

---

## 📚 Documentation Features

* **Edit on GitHub:** “Edit” button at the top of each page.
* **Versioned Docs:** Switch between different releases.
* **Instant Search & Custom 404 page.**

---

## 🤝 Contributing

See [CONTRIBUTING.md](../CONTRIBUTING.md) for coding standards and contributing steps.

---

## Useful Links

* [Copier Documentation](https://copier.readthedocs.io/)
* \[Template Repository]\([https://github.com/your-org/{{](https://github.com/your-org/{{) project\_slug }})

