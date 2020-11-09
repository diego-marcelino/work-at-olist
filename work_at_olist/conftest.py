import pytest

from work_at_olist.authors.models import Author
from work_at_olist.authors.tests.factories import AuthorFactory


@pytest.fixture(autouse=True)
def media_storage(settings, tmpdir):
    """Media storage for pytest."""
    settings.MEDIA_ROOT = tmpdir.strpath


@pytest.fixture
def author() -> Author:
    """Returns an author instance."""
    return AuthorFactory()
