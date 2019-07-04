import pytest


@pytest.fixture(scope="session")
def vcr_config():
    """Overwrite headers where key can be leaked"""
    return {
        "filter_headers": [("authorization", "DUMMY")],
    }
