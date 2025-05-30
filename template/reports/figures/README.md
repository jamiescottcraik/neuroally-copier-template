Here’s a straight-talking, ready-to-drop `reports/figures/README.md` for your GoldSTAR template.
It tells users *exactly* what goes where, and why.
No waffle.

---

```markdown
# Figures

This folder is for all plots, charts, visual outputs, or diagrams generated as part of the {{ project_name }} project.

---

## 📈 How to Use

- **Save figures from notebooks or scripts here.**
- Use meaningful filenames:
  `confusion-matrix.png`, `embedding-visualization.svg`, `pipeline-diagram.pdf`, etc.
- Organize with subfolders if needed (`figures/results/`, `figures/data-viz/`).

---

## 📝 Best Practices

- Keep all *source code* for generating plots in `notebooks/` or `src/`, not here.
- Never commit huge, uncompressed image files—optimize before adding.
- For publication, add captions or brief notes in a Markdown file alongside key figures.

---

## 📋 Example Layout

```

reports/
└── figures/
├── confusion-matrix.png
├── roc-curve.svg
├── architecture-diagram.pdf
└── README.md   # (this file)

```

---

If you use figures in reports or docs, link to or embed from here.

---
