# Jupyter Notebooks

This folder contains example and exploratory notebooks for **{{ project_name }}**.

---

## 🚦 Getting Started

- **Open `00-getting-started.ipynb` first**
  Walks you through setup, API config, and running your first provider example.

- All notebooks use the project’s `src/` modules and are ready to run if you’ve installed the environment (`poetry install` or `conda` + `poetry install`).

---

## 📚 Adding New Notebooks

- Use the `01-`, `02-` numbering scheme for clarity (`01-data-exploration.ipynb`, `02-train-model.ipynb`, etc.).
- Keep notebooks focused:
  *one topic, one use case per file*.

- Import project code like:
  ```python
  from src.providers import ...
````

---

## ⚡ Best Practices

* Restart kernel and run all cells before committing.
* Don’t commit big data, models, or outputs—keep notebooks lightweight.
* Reference this folder in your main `README.md` or docs for new users.

---

For questions or ideas, see [CONTRIBUTING.md](../CONTRIBUTING.md).

---
