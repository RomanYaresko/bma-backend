from django.db.models import QuerySet
from rest_framework.permissions import SAFE_METHODS, BasePermission, IsAdminUser, IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from api.models.author import Author
from api.serializers.author import AuthorSerializer


class AuthorViewSet(ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    permission_classes = [IsAuthenticated]

    def get_permissions(self) -> list[BasePermission]:
        permissions = super().get_permissions()

        if self.request.method not in SAFE_METHODS:
            permissions.append(IsAdminUser())

        return permissions

    def filter_queryset(self, queryset: QuerySet[Author]) -> QuerySet[Author]:
        queryset = super().filter_queryset(queryset)
        queryset.order_by("name")
        return queryset
