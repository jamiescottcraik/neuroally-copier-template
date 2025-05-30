# Project Playground

Welcome to the Playground!
This space is for **trying out, tweaking, and extending** {{ project_name }} before you commit to any one workflow or provider.

---

## ⚡ What Can You Do Here?

- **Test provider integrations:** Use the built-in connectors for {{ main_category }} and other APIs.
- **Prototype pipelines:** Combine models, APIs, and utilities in the `src/` directory.
- **Explore code structure:** Learn how modularity and config management works in this template.
- **Run example scripts:** Use and adapt starter scripts in `src/`.

---

## 🚦 Quickstart: Running the Playground

1. **Set up your environment:**
    - See [Getting Started](index.md#getting-started) for Poetry, Conda, or UV setup.

2. **Navigate to your project directory:**
    ```bash
    cd {{ project_slug }}
    ```

3. **Find example code:**
    - Main entrypoint: `src/main.py`
    - Provider examples: `src/providers/{{ main_category }}/example.py`

4. **Run a sample provider script:**
    ```bash
    poetry run python src/main.py --provider {{ main_category }} --action demo
    ```
    - Use `--help` to see all CLI options.

---

## 🧰 Example: Calling a Provider

If you selected `llms` and the provider is `openai`, try:

```bash
poetry run python src/main.py --provider llms --model gpt-4 --prompt "Say hello, world!"
````

Or edit `src/providers/llms/example.py` to experiment with your own prompts and models.

---

## 📁 Where to Put Your Playground Experiments

* Put temporary scripts or notebooks in a `playground/` directory (create it if it doesn't exist).
* Keep reusable examples in `examples/` or inside the appropriate `src/providers/` subfolder.

---

## 📝 Best Practices

* **Reset often:** Clean up your playground directory as you go.
* **Share what works:** Add Markdown docs or code snippets to share valuable patterns.
* **Follow project conventions:** Keep code style consistent with [CONTRIBUTING.md](../CONTRIBUTING.md).

---

## 🔗 Related Docs

* [Docs Home](index.md)
* [Provider API Overview](provider_api_overview.md)
* [CONTRIBUTING.md](../CONTRIBUTING.md)

---

**Break stuff, build fast, and make it better—
that’s what the Playground is for.**
