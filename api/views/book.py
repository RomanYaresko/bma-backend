from django.db.models import QuerySet
from rest_framework.permissions import BasePermission, IsAuthenticated
from rest_framework.serializers import BaseSerializer
from rest_framework.viewsets import ModelViewSet

from api.models.book import Book
from api.permissions.book_creator_permission import IsBookCreatorOrReadOnly
from api.serializers.book import BookCreateSerializer, BookSerializer, BookUpdateSerializer


class BookViewSet(ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]

    def filter_queryset(self, queryset: QuerySet[Book]) -> QuerySet[Book]:
        queryset = super().filter_queryset(queryset)
        order = self.request.GET.get("order")

        if order == "title":
            queryset = queryset.order_by("title")

        if order == "creator":
            queryset = queryset.order_by("creator__given_name")

        if order == "author":
            queryset = queryset.order_by("author__name")

        return queryset

    def get_serializer_class(self) -> BaseSerializer:
        if self.action == "create":
            return BookCreateSerializer

        if self.action == "update":
            return BookUpdateSerializer

        return BookSerializer

    def get_permissions(self) -> list[BasePermission]:
        permissions = super().get_permissions()

        if self.action == "update":
            permissions.append(IsBookCreatorOrReadOnly())

        return permissions
