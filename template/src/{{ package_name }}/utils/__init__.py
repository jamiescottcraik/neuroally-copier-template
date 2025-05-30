"""
src.utils

General-purpose helper functions and shared utilities for {{ project_name }}.

- Put only generic, reusable logic here (not project-specific business logic).
- Keep functions short, typed, and well-documented.
- Import what you need in features, data, api, etc.

Example usage:
    from src.utils import slugify
"""


def slugify(text: str) -> str:
    """Convert text to a URL-safe slug."""
    return text.lower().replace(" ", "-").replace("_", "-").strip("-")


# Add more utilities below as your project grows.
