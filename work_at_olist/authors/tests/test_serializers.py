import pytest
from factory import Faker
from rest_framework.exceptions import ValidationError

from ..serializers import AuthorSerializer

pytestmark = pytest.mark.django_db


def test_create_author():
    """Test create a client with current user as owner."""
    data = {'name': Faker('name').generate()}
    serializer = AuthorSerializer(data=data)
    serializer.is_valid(raise_exception=True)
    author = serializer.save()
    assert author.id


def test_create_author_no_name_validation_error():
    """Test empty name causes validation error."""
    data = {'name': ''}
    serializer = AuthorSerializer(data=data)
    with pytest.raises(ValidationError):
        serializer.is_valid(raise_exception=True)


def test_serialize_author_to_dictionary(author):
    """Test client object is properly serialized."""
    serializer = AuthorSerializer(author)
    output_fields = {'id', 'name'}
    assert output_fields == set(serializer.data)
