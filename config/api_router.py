from django.conf import settings
from rest_framework.routers import DefaultRouter
from rest_framework.routers import SimpleRouter

from work_at_olist.authors.viewsets import AuthorViewSet

if settings.DEBUG:
    router = DefaultRouter()
else:
    router = SimpleRouter()

router.register('authors', AuthorViewSet, basename='authors')

app_name = 'api-v1'
urlpatterns = router.urls
