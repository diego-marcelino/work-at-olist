from django.contrib import admin

from .models import Book


@admin.register(Book)
class AuthorAdmin(admin.ModelAdmin):
    """Administration page for book model."""

    list_display = (
        'name',
        'edition',
        'publication_year',
    )
    search_fields = (
        'name',
        'edition',
        'publication_year',
    )
