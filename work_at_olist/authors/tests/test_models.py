import pytest

pytestmark = pytest.mark.django_db


def test_string_representation(author):
    """Check author string representation."""
    assert str(author) == author.name
