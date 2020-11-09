from rest_framework import serializers

from .models import Author


class AuthorSerializer(serializers.ModelSerializer):
    """Authors serializer."""

    class Meta:
        """Meta information for author serializer."""
        model = Author
        fields = (
            'id',
            'name',
        )
