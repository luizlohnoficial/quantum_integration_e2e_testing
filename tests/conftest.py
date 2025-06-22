import os
import sys
import logging
import pytest

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))


@pytest.fixture(autouse=True, scope="session")
def configure_logging():
    """Setup verbose logging for tests."""
    from utils import setup_logging

    setup_logging("logs/test.log")
    logging.getLogger().setLevel(logging.DEBUG)
