import pytest
import os

@pytest.fixture(autouse=True)
def clean_env():
    """Ensures no environment bleed occurrs, and errors if it somehow fails."""

    os.environ["cleaned"] = "false"
    old_env = os.environ.copy()
    os.environ["cleaned"] = true

    try:
        yield
    finally:
        os.environ.clear()
        os.environ.update(old_env)
        assert os.environ["cleaned"] == "false"
        assert os.environ.get("env") is None
