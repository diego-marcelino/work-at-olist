import pytest
from factory import Faker
from rest_framework import status

from ..viewsets import AuthorViewSet

pytestmark = pytest.mark.django_db
CT_JSON = 'application/json; charset=utf-8'


def test_create_status_201(rf):
    """Test create method should return status code 201."""
    view = AuthorViewSet.as_view({'post': 'create'})
    payload = {'name': Faker('name').generate()}
    request = rf.post('/fake-url/', data=payload)
    response = view(request)
    assert response.status_code == status.HTTP_201_CREATED


def test_create_no_name_status_400(rf):
    """Test create method with no name should return status code 400."""
    view = AuthorViewSet.as_view({'post': 'create'})
    payload = {'name': ''}
    request = rf.post('/fake-url/', data=payload)
    response = view(request)
    assert response.status_code == status.HTTP_400_BAD_REQUEST


def test_list_all_status_200(rf):
    """Test list method should return status code 200."""
    view = AuthorViewSet.as_view({'get': 'list'})
    request = rf.get('/fake-url/')
    response = view(request)
    assert response.status_code == status.HTTP_200_OK


def test_retrieve_status_200(rf, author):
    """Test retrieve method should return status code 200."""
    view = AuthorViewSet.as_view({'get': 'retrieve'})
    request = rf.get('/fake-url/')
    response = view(request, pk=author.id)
    assert response.status_code == status.HTTP_200_OK


def test_retrieve_invalid_id_status_404(rf):
    """Test retrieve method with invalid id should return status code 404."""
    view = AuthorViewSet.as_view({'get': 'retrieve'})
    request = rf.get('/fake-url/')
    response = view(request, pk=0)
    assert response.status_code == status.HTTP_404_NOT_FOUND


def test_update_status_200(rf, author):
    """Test update method should return status code 200."""
    view = AuthorViewSet.as_view({'put': 'update'})
    payload = {'name': Faker('name').generate()}
    request = rf.put('/fake-url/', data=payload, content_type=CT_JSON)
    response = view(request, pk=author.id)
    assert response.status_code == status.HTTP_200_OK


def test_update_no_name_status_400(rf, author):
    """Test update method with no name should return status code 400."""
    view = AuthorViewSet.as_view({'put': 'update'})
    payload = {'name': ''}
    request = rf.put('/fake-url/', data=payload, content_type=CT_JSON)
    response = view(request, pk=author.id)
    assert response.status_code == status.HTTP_400_BAD_REQUEST


def test_update_invalid_id_status_404(rf):
    """Test update method with invalid id should return status code 404."""
    view = AuthorViewSet.as_view({'put': 'update'})
    payload = {'name': Faker('name').generate()}
    request = rf.put('/fake-url/', data=payload, content_type=CT_JSON)
    response = view(request, pk=0)
    assert response.status_code == status.HTTP_404_NOT_FOUND


def test_partial_update_status_200(rf, author):
    """Test partial update method should return status code 200."""
    view = AuthorViewSet.as_view({'patch': 'partial_update'})
    payload = {'name': Faker('name').generate()}
    request = rf.patch('/fake-url/', data=payload, content_type=CT_JSON)
    response = view(request, pk=author.id)
    assert response.status_code == status.HTTP_200_OK


def test_partial_update_no_name_status_400(rf, author):
    """Test partial update with no name should return status code 400."""
    view = AuthorViewSet.as_view({'patch': 'partial_update'})
    payload = {'name': ''}
    request = rf.patch('/fake-url/', data=payload, content_type=CT_JSON)
    response = view(request, pk=author.id)
    assert response.status_code == status.HTTP_400_BAD_REQUEST


def test_partial_update_invalid_id_status_404(rf):
    """Test partial update with invalid id should return status code 404."""
    view = AuthorViewSet.as_view({'patch': 'partial_update'})
    payload = {'name': ''}
    request = rf.patch('/fake-url/', data=payload, content_type=CT_JSON)
    response = view(request, pk=0)
    assert response.status_code == status.HTTP_404_NOT_FOUND


def test_delete_status_204(rf, author):
    """Test delete method should return status code 204."""
    view = AuthorViewSet.as_view({'delete': 'destroy'})
    request = rf.delete('/fake-url/')
    response = view(request, pk=author.id)
    assert response.status_code == status.HTTP_204_NO_CONTENT


def test_delete_invalid_id_status_404(rf):
    """Test delete method with invalid id should return status code 404."""
    view = AuthorViewSet.as_view({'delete': 'destroy'})
    request = rf.delete('/fake-url/')
    response = view(request, pk=0)
    assert response.status_code == status.HTTP_404_NOT_FOUND
