from django.conf import settings
from rest_framework.routers import DefaultRouter
from rest_framework.routers import SimpleRouter

from work_at_olist.authors.viewsets import AuthorViewSet
from work_at_olist.books.viewsets import BookViewSet

if settings.DEBUG:
    router = DefaultRouter()
else:
    router = SimpleRouter()

router.register('authors', AuthorViewSet, basename='authors')
router.register('books', BookViewSet, basename='books')

app_name = 'api-v1'
urlpatterns = router.urls
