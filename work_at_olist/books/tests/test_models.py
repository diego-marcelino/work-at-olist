import pytest

pytestmark = pytest.mark.django_db


def test_string_representation(book):
    """Check book string representation."""
    assert str(book) == f'{book.name} | Ed. #{book.edition}'


def test_related_field(book):
    """Check book may be found on author books list."""
    for author in book.authors.all():
        assert book in author.books.all()
