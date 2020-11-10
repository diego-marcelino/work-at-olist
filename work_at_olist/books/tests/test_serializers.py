import pytest
from factory import Faker
from rest_framework.exceptions import ValidationError

from ..serializers import BookSerializer

pytestmark = pytest.mark.django_db


def test_create_book(author):
    """Test create a book."""
    data = {
        'name': Faker('sentence', nb_words=4).generate(),
        'edition': 1,
        'publication_year': 2020,
        'authors': [author.id]
    }
    serializer = BookSerializer(data=data)
    serializer.is_valid(raise_exception=True)
    book = serializer.save()
    assert book.id


def test_create_book_invalid_name_validation_error(author):
    """Test create a book with invalid name raises validation error."""
    data = {
        'name': '',
        'edition': 1,
        'publication_year': 2020,
        'authors': [author.id]
    }
    serializer = BookSerializer(data=data)
    with pytest.raises(ValidationError) as e:
        serializer.is_valid(raise_exception=True)
    assert 'name' in e.value.detail


def test_create_book_invalid_edition_validation_error(author):
    """Test create a book with invalid edition raises validation error."""
    data = {
        'name': Faker('sentence', nb_words=4).generate(),
        'edition': 0,
        'publication_year': 2020,
        'authors': [author.id]
    }
    serializer = BookSerializer(data=data)
    with pytest.raises(ValidationError) as e:
        serializer.is_valid(raise_exception=True)
    assert 'edition' in e.value.detail


def test_create_book_invalid_publication_year_validation_error(author):
    """Test create a book with invalid edition raises validation error."""
    data = {
        'name': Faker('sentence', nb_words=4).generate(),
        'edition': 1,
        'publication_year': 0,
        'authors': [author.id]
    }
    serializer = BookSerializer(data=data)
    with pytest.raises(ValidationError) as e:
        serializer.is_valid(raise_exception=True)
    assert 'publication_year' in e.value.detail


def test_create_book_invalid_author_id_validation_error():
    """Test create a book with invalid author id raises validation error."""
    data = {
        'name': Faker('sentence', nb_words=4).generate(),
        'edition': 1,
        'publication_year': 2020,
        'authors': [0]
    }
    serializer = BookSerializer(data=data)
    with pytest.raises(ValidationError) as e:
        serializer.is_valid(raise_exception=True)
    assert 'authors' in e.value.detail


def test_serialize_book_to_dictionary(book):
    """Test book object is properly serialized."""
    serializer = BookSerializer(book)
    output_fields = {'id', 'name', 'edition', 'publication_year', 'authors'}
    assert output_fields == set(serializer.data)
