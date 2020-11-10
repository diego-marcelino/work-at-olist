from random import randint
from sys import maxsize

import pytest
from django.urls import resolve
from django.urls import reverse

pytestmark = pytest.mark.django_db


def test_author_list_url():
    """Test authors endpoint url for get and post methods."""
    view_name = 'api-v1:authors-list'
    path = '/api/v1/authors/'
    assert reverse(view_name) == path
    assert resolve(path).view_name == view_name


def test_author_detail_url():
    """Test authors endpoint url for get, put, patch and delete methods."""
    author_id = randint(1, maxsize)
    view_name = 'api-v1:authors-detail'
    path = f'/api/v1/authors/{author_id}/'
    assert reverse(view_name, kwargs={'pk': author_id}) == path
    assert resolve(path).view_name == view_name
