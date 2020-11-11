from random import randint
from sys import maxsize

import pytest
from django.urls import resolve
from django.urls import reverse

pytestmark = pytest.mark.django_db


def test_book_list_url():
    """Test books endpoint url for get and post methods."""
    view_name = 'api-v1:books-list'
    path = '/api/v1/books/'
    assert reverse(view_name) == path
    assert resolve(path).view_name == view_name


def test_book_detail_url():
    """Test books endpoint url for get, put, patch and delete methods."""
    book_id = randint(1, maxsize)
    view_name = 'api-v1:books-detail'
    path = f'/api/v1/books/{book_id}/'
    assert reverse(view_name, kwargs={'pk': book_id}) == path
    assert resolve(path).view_name == view_name
