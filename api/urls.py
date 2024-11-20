from django.urls import include, path
from rest_framework.routers import DefaultRouter

from api.views.author import AuthorViewSet
from api.views.book import BookViewSet

router = DefaultRouter()
router.register("author", AuthorViewSet)
router.register("book", BookViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
