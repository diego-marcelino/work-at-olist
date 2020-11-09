from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class AuthorsAppConfig(AppConfig):
    """Config for authors app."""

    name = 'work_at_olist.authors'
    label = 'work_at_olist.authors'
    verbose_name = _('Authors')
