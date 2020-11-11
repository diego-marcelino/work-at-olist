from django.utils.translation import gettext_lazy as _
from django_filters import rest_framework as filters
from rest_framework.viewsets import ModelViewSet

from .models import Book
from .serializers import BookSerializer


class BookFilter(filters.FilterSet):
    """Filter for books."""

    name = filters.CharFilter(field_name='name', lookup_expr='icontains',
                              help_text=_('Filter by any part of book name'))
    publication_year = filters.NumberFilter(
        field_name='publication_year',
        help_text=_('Filter by book publication year'))
    edition = filters.NumberFilter(field_name='edition',
                                   help_text=_('Filter by book edition number'))
    author = filters.NumberFilter(field_name='authors', lookup_expr='id',
                                  help_text=_('Filter by author id'))

    class Meta:
        """Meta info for book filter."""
        model = Book
        fields = (
            'name',
            'publication_year',
            'edition',
            'author',
        )


class BookViewSet(ModelViewSet):
    """Book view set.

    create:
    Create a new book.

    retrieve:
    Get a specific book information according to its id.

    list:
    Retrieve a paginated list of books. Filter by any part of book name,
    publication year, edition and author id.

    update:
    Update an book information.

    partial_update:
    Partially update a book information.

    destroy:
    Delete an book.
    """

    serializer_class = BookSerializer
    queryset = Book.objects.all()
    filterset_class = BookFilter
