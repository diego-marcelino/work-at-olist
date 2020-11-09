from io import StringIO
from unittest.mock import mock_open
from unittest.mock import patch

import pytest
from django.core.management import call_command

from ..models import Author

pytestmark = pytest.mark.django_db
AUTHORS_CSV = ('name\n'
               'Luciano Ramalho\n'
               'Osvaldo Santana Neto\n'
               'David Beazley\n'
               'Chetan Giridhar\n'
               'Brian K. Jones\n'
               'J.K Rowling\n')


@patch('builtins.open', mock_open(read_data=AUTHORS_CSV))
def test_create_authors():
    """Test if authors are saved on database."""
    call_command('import_authors', 'fake_file_path.csv')
    for name in AUTHORS_CSV.split('\n')[1:-1]:
        author = Author.objects.get(name=name.strip())
        assert author.id


def test_invalid_file_path():
    """Tests invalid file path."""
    with StringIO() as stdout:
        call_command('import_authors', 'fake_file_path.csv', stdout=stdout)
        output = stdout.getvalue()
    assert 'Invalid file path' in output
