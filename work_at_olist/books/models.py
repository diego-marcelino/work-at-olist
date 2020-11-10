from django.core.validators import MinValueValidator
from django.db import models
from django.utils.translation import gettext_lazy as _

from work_at_olist.authors.models import Author


class Book(models.Model):
    """Book model."""

    name = models.CharField(_('Name of the book'), max_length=100,
                            help_text=_('Name of the book'))
    edition = models.IntegerField(_('Edition number'),
                                  validators=(MinValueValidator(1),),
                                  help_text=_('Edition number'))
    publication_year = models.IntegerField(
        _('Publication year of the book'),
        validators=(MinValueValidator(1800),),
        help_text=_('Publication year of the book'))
    authors = models.ManyToManyField(to=Author,
                                     verbose_name=_('Authors of the book'),
                                     related_name='books',
                                     blank=False,
                                     help_text=_('List of authors of book'))

    class Meta:
        """Meta info for book model."""
        verbose_name = _('book')
        verbose_name_plural = _('books')

    def __str__(self):
        """Return string representation."""
        return f'{self.name} | Ed. #{self.edition}'
