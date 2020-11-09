from django.db import models
from django.utils.translation import gettext_lazy as _


class Author(models.Model):
    """Author model."""

    name = models.CharField(_('Name of the author'), max_length=100,
                            help_text=_('Name of the author'))

    class Meta:
        """Meta info for author model."""
        verbose_name = _('author')
        verbose_name_plural = _('authors')

    def __str__(self):
        """Return string representation."""
        return self.name
