from factory import Faker
from factory.django import DjangoModelFactory

from ..models import Author


class AuthorFactory(DjangoModelFactory):
    """Factory for author model."""

    name = Faker('name')

    class Meta:
        """Meta class for author factory."""
        model = Author
