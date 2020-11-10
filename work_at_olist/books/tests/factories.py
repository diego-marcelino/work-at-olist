from random import randint

from factory import Faker
from factory import post_generation
from factory.django import DjangoModelFactory

from ..models import Book
from work_at_olist.authors.tests.factories import AuthorFactory


class BookFactory(DjangoModelFactory):
    """Factory for book model."""

    name = Faker('sentence', nb_words=4)
    edition = Faker('pyint', min_value=1, max_value=100)
    publication_year = Faker('pyint', min_value=1900, max_value=2050)

    @post_generation
    def authors(self, create, extracted, **kwargs):
        """Post generation for adding the book authors."""
        if not create:
            # Simple build, do nothing.
            return
        if extracted:
            # A list of authors were passed in, use them
            for author in extracted:
                self.authors.add(author)
        else:
            for _ in range(randint(1, 5)):
                self.authors.add(AuthorFactory())

    class Meta:
        """Meta class for book factory."""
        model = Book
