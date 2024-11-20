from django.contrib.auth import get_user_model
from django.db import models

from api.models.author import Author


class Book(models.Model):
    creator = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    cover = models.ImageField(upload_to="book_covers")

    def __str__(self) -> str:
        return super().__str__()
