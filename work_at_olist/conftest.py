import pytest

from work_at_olist.authors.models import Author
from work_at_olist.authors.tests.factories import AuthorFactory
from work_at_olist.books.models import Book
from work_at_olist.books.tests.factories import BookFactory


@pytest.fixture(autouse=True)
def media_storage(settings, tmpdir):
    """Media storage for pytest."""
    settings.MEDIA_ROOT = tmpdir.strpath


@pytest.fixture
def author() -> Author:
    """Returns an author instance."""
    return AuthorFactory()


@pytest.fixture
def book() -> Book:
    """Returns a book instance."""
    return BookFactory()
