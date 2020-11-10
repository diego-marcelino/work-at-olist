from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class BooksAppConfig(AppConfig):
    """Config for books app."""

    name = 'work_at_olist.books'
    verbose_name = _('Books')
