from django.db import models


class Author(models.Model):
    name = models.CharField(unique=True, max_length=255)
    birth_date = models.DateField()

    def __str__(self) -> str:
        return self.name
