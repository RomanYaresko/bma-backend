from typing import Any

from rest_framework import serializers

from api.models.author import Author
from api.models.book import Book
from api.serializers.author import AuthorSerializer
from user.serializers.custom_user import CustomUserSerializer


class BookSerializer(serializers.ModelSerializer):
    creator = CustomUserSerializer(read_only=True)
    author = AuthorSerializer(read_only=True)

    class Meta:
        model = Book
        fields = [
            "id",
            "creator",
            "title",
            "author",
            "cover",
        ]


class BookCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = [
            "title",
            "author",
            "cover",
        ]

    def create(self, validated_data: dict[str, Any]) -> Book:
        validated_data["creator"] = self.context.get("request").user
        return super().create(validated_data)


class BookUpdateSerializer(serializers.ModelSerializer):
    title = serializers.CharField(required=False)
    author = serializers.PrimaryKeyRelatedField(queryset=Author.objects.all(), required=False)
    cover = serializers.FileField(required=False)

    class Meta:
        model = Book
        fields = [
            "title",
            "author",
            "cover",
        ]
