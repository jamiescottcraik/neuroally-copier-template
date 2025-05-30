"""
Basic example test for {{ project_name }}.
Use this file to bootstrap real tests and CI checks.
"""

import pytest
from src.config.settings import settings


def test_env_loaded():
    """Check the .env and settings are loaded (smoke test)."""
    # This should always be True if your .env and settings.py are correct
    assert settings is not None
    # Check MAIN_CATEGORY is set
    assert settings.MAIN_CATEGORY != "", "MAIN_CATEGORY should not be blank"


def test_addition():
    """Dummy math test, safe to remove."""
    assert 2 + 2 == 4
