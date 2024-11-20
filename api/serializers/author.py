from rest_framework import serializers

from api.models.author import Author


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = [
            "id",
            "name",
            "birth_date",
        ]
