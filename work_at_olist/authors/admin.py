from django.contrib import admin

from .models import Author


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    """Administration page for author model."""

    list_display = (
        'name',
        'id',
    )
    search_fields = ('name',)
