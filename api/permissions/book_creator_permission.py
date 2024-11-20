from typing import Any

from rest_framework import permissions
from rest_framework.request import HttpRequest

from api.models.book import Book


class IsBookCreatorOrReadOnly(permissions.BasePermission):
    def has_permission(self, request: HttpRequest, view: Any) -> bool:
        return super().has_permission(request, view)

    def has_object_permission(self, request: HttpRequest, _: Any, obj: Book) -> bool:
        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.creator == request.user
