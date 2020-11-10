from django.utils.translation import gettext_lazy as _
from rest_framework import serializers

from .models import Book
from work_at_olist.authors.models import Author


class BookSerializer(serializers.ModelSerializer):
    """Books serializer."""

    authors = serializers.PrimaryKeyRelatedField(
        many=True,
        required=True,
        queryset=Author.objects.all(),
        help_text=_('List of author ids'))

    class Meta:
        """Meta information for book serializer."""
        model = Book
        fields = (
            'id',
            'name',
            'edition',
            'publication_year',
            'authors',
        )
