from django.utils.translation import gettext_lazy as _
from django_filters import rest_framework as filters
from rest_framework.viewsets import ModelViewSet

from .models import Author
from .serializers import AuthorSerializer


class AuthorFilter(filters.FilterSet):
    """Filter for authors."""

    name = filters.CharFilter(field_name='name', lookup_expr='icontains',
                              help_text=_('Filter by any part of author name'))

    class Meta:
        """Meta info for author filter."""
        model = Author
        fields = ('name',)


class AuthorViewSet(ModelViewSet):
    """Author view set.

    create:
    Create a new author.

    retrieve:
    Get a specific author information according to its id.

    list:
    Retrieve a paginated list of authors. Filter by any part of author name.

    update:
    Update an author information.

    partial_update:
    Partially update an author information.

    destroy:
    Delete an author.
    """

    serializer_class = AuthorSerializer
    queryset = Author.objects.all()
    filterset_class = AuthorFilter
