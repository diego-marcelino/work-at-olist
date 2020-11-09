import pytest


@pytest.fixture(autouse=True)
def media_storage(settings, tmpdir):
    """Media storage for pytest."""
    settings.MEDIA_ROOT = tmpdir.strpath
