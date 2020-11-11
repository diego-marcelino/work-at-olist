import pytest
from factory import Faker
from rest_framework import status

from ..viewsets import BookViewSet

pytestmark = pytest.mark.django_db
CT_JSON = 'application/json; charset=utf-8'

# Create


def test_create_status_201(rf, author):
    """Test create method should return status code 201."""
    view = BookViewSet.as_view({'post': 'create'})
    payload = {
        'name': Faker('sentence', nb_words=4).generate(),
        'edition': 1,
        'publication_year': 2020,
        'authors': [author.id]
    }
    request = rf.post('/fake-url/', data=payload)
    response = view(request)
    assert response.status_code == status.HTTP_201_CREATED


def test_create_no_name_status_400(rf, author):
    """Test create method with no name should return status code 400."""
    view = BookViewSet.as_view({'post': 'create'})
    payload = {
        'name': '',
        'edition': 1,
        'publication_year': 2020,
        'authors': [author.id]
    }
    request = rf.post('/fake-url/', data=payload)
    response = view(request)
    assert response.status_code == status.HTTP_400_BAD_REQUEST


def test_create_invalid_edition_status_400(rf, author):
    """Test create with invalid edition should return status code 400."""
    view = BookViewSet.as_view({'post': 'create'})
    payload = {
        'name': Faker('sentence', nb_words=4).generate(),
        'edition': 0,
        'publication_year': 2020,
        'authors': [author.id]
    }
    request = rf.post('/fake-url/', data=payload)
    response = view(request)
    assert response.status_code == status.HTTP_400_BAD_REQUEST


def test_create_invalid_publication_year_status_400(rf, author):
    """Test create with invalid publication year return status code 400."""
    view = BookViewSet.as_view({'post': 'create'})
    payload = {
        'name': Faker('sentence', nb_words=4).generate(),
        'edition': 1,
        'publication_year': 0,
        'authors': [author.id]
    }
    request = rf.post('/fake-url/', data=payload)
    response = view(request)
    assert response.status_code == status.HTTP_400_BAD_REQUEST


def test_create_invalid_author_id_status_400(rf):
    """Test create with invalid publication year return status code 400."""
    view = BookViewSet.as_view({'post': 'create'})
    payload = {
        'name': Faker('sentence', nb_words=4).generate(),
        'edition': 1,
        'publication_year': 2020,
        'authors': [0]
    }
    request = rf.post('/fake-url/', data=payload)
    response = view(request)
    assert response.status_code == status.HTTP_400_BAD_REQUEST


# List


def test_list_all_status_200(rf):
    """Test list method should return status code 200."""
    view = BookViewSet.as_view({'get': 'list'})
    request = rf.get('/fake-url/')
    response = view(request)
    assert response.status_code == status.HTTP_200_OK


# Retrieve


def test_retrieve_status_200(rf, book):
    """Test retrieve method should return status code 200."""
    view = BookViewSet.as_view({'get': 'retrieve'})
    request = rf.get('/fake-url/')
    response = view(request, pk=book.id)
    assert response.status_code == status.HTTP_200_OK


def test_retrieve_invalid_id_status_404(rf):
    """Test retrieve method with invalid id should return status code 404."""
    view = BookViewSet.as_view({'get': 'retrieve'})
    request = rf.get('/fake-url/')
    response = view(request, pk=0)
    assert response.status_code == status.HTTP_404_NOT_FOUND


# Update


def test_update_status_200(rf, book, author):
    """Test update method should return status code 200."""
    view = BookViewSet.as_view({'put': 'update'})
    payload = {
        'name': Faker('sentence', nb_words=4).generate(),
        'edition': 1,
        'publication_year': 2020,
        'authors': [author.id]
    }
    request = rf.put('/fake-url/', data=payload, content_type=CT_JSON)
    response = view(request, pk=book.id)
    assert response.status_code == status.HTTP_200_OK


def test_update_invalid_id_status_404(rf, author):
    """Test update method with invalid id should return status code 404."""
    view = BookViewSet.as_view({'put': 'update'})
    payload = {
        'name': Faker('sentence', nb_words=4).generate(),
        'edition': 1,
        'publication_year': 2020,
        'authors': [author.id]
    }
    request = rf.put('/fake-url/', data=payload, content_type=CT_JSON)
    response = view(request, pk=0)
    assert response.status_code == status.HTTP_404_NOT_FOUND


def test_update_no_name_status_400(rf, book, author):
    """Test update method with no name should return status code 400."""
    view = BookViewSet.as_view({'put': 'update'})
    payload = {
        'name': '',
        'edition': 1,
        'publication_year': 2020,
        'authors': [author.id]
    }
    request = rf.put('/fake-url/', data=payload, content_type=CT_JSON)
    response = view(request, pk=book.id)
    assert response.status_code == status.HTTP_400_BAD_REQUEST


def test_update_invalid_edition_status_400(rf, book, author):
    """Test update method invalid edition should return status code 400."""
    view = BookViewSet.as_view({'put': 'update'})
    payload = {
        'name': Faker('sentence', nb_words=4).generate(),
        'edition': 0,
        'publication_year': 2020,
        'authors': [author.id]
    }
    request = rf.put('/fake-url/', data=payload, content_type=CT_JSON)
    response = view(request, pk=book.id)
    assert response.status_code == status.HTTP_400_BAD_REQUEST


def test_update_invalid_publication_year_status_400(rf, book, author):
    """Test update method invalid publication year return status code 400."""
    view = BookViewSet.as_view({'put': 'update'})
    payload = {
        'name': Faker('sentence', nb_words=4).generate(),
        'edition': 1,
        'publication_year': 0,
        'authors': [author.id]
    }
    request = rf.put('/fake-url/', data=payload, content_type=CT_JSON)
    response = view(request, pk=book.id)
    assert response.status_code == status.HTTP_400_BAD_REQUEST


def test_update_invalid_author_id_status_400(rf, book):
    """Test update method invalid publication year return status code 400."""
    view = BookViewSet.as_view({'put': 'update'})
    payload = {
        'name': Faker('sentence', nb_words=4).generate(),
        'edition': 1,
        'publication_year': 2020,
        'authors': [0]
    }
    request = rf.put('/fake-url/', data=payload, content_type=CT_JSON)
    response = view(request, pk=book.id)
    assert response.status_code == status.HTTP_400_BAD_REQUEST


# Partial update
def test_partial_update_name_status_200(rf, book):
    """Test partial update method should return status code 200."""
    view = BookViewSet.as_view({'patch': 'partial_update'})
    payload = {'name': Faker('sentence', nb_words=4).generate()}
    request = rf.patch('/fake-url/', data=payload, content_type=CT_JSON)
    response = view(request, pk=book.id)
    assert response.status_code == status.HTTP_200_OK


def test_partial_update_edition_status_200(rf, book):
    """Test partial update method should return status code 200."""
    view = BookViewSet.as_view({'patch': 'partial_update'})
    payload = {'edition': 10}
    request = rf.patch('/fake-url/', data=payload, content_type=CT_JSON)
    response = view(request, pk=book.id)
    assert response.status_code == status.HTTP_200_OK


def test_partial_update_publication_year_status_200(rf, book):
    """Test partial update method should return status code 200."""
    view = BookViewSet.as_view({'patch': 'partial_update'})
    payload = {'publication_year': 1990}
    request = rf.patch('/fake-url/', data=payload, content_type=CT_JSON)
    response = view(request, pk=book.id)
    assert response.status_code == status.HTTP_200_OK


def test_partial_update_authors_status_200(rf, book, author):
    """Test partial update method should return status code 200."""
    view = BookViewSet.as_view({'patch': 'partial_update'})
    payload = {'authors': [author.id]}
    request = rf.patch('/fake-url/', data=payload, content_type=CT_JSON)
    response = view(request, pk=book.id)
    assert response.status_code == status.HTTP_200_OK
    """Test partial update with no name should return status code 400."""
    view = BookViewSet.as_view({'patch': 'partial_update'})
    payload = {
        'name': '',
        'edition': 1,
        'publication_year': 2020,
        'authors': [author.id]
    }
    request = rf.patch('/fake-url/', data=payload, content_type=CT_JSON)
    response = view(request, pk=book.id)
    assert response.status_code == status.HTTP_400_BAD_REQUEST


def test_partial_update_invalid_id_status_404(rf):
    """Test partial update with invalid id should return status code 404."""
    view = BookViewSet.as_view({'patch': 'partial_update'})
    payload = {'name': ''}
    request = rf.patch('/fake-url/', data=payload, content_type=CT_JSON)
    response = view(request, pk=0)
    assert response.status_code == status.HTTP_404_NOT_FOUND


# Delete


def test_delete_status_204(rf, book):
    """Test delete method should return status code 204."""
    view = BookViewSet.as_view({'delete': 'destroy'})
    request = rf.delete('/fake-url/')
    response = view(request, pk=book.id)
    assert response.status_code == status.HTTP_204_NO_CONTENT


def test_delete_invalid_id_status_404(rf):
    """Test delete method with invalid id should return status code 404."""
    view = BookViewSet.as_view({'delete': 'destroy'})
    request = rf.delete('/fake-url/')
    response = view(request, pk=0)
    assert response.status_code == status.HTTP_404_NOT_FOUND
