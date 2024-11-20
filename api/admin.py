from typing import Any

from django.contrib import admin
from django.utils.html import format_html

from api.models.author import Author
from api.models.book import Book


class BookAdmin(admin.ModelAdmin):
    model = Book
    list_display = [
        "id",
        "title",
        "author",
        "cover_tag",
    ]

    def cover_tag(self, obj: Book) -> Any:
        return format_html(
            f'<img src="{obj.cover.url if obj.cover else ''}" style="max-width:100px; max-height:100px"/>'
        )


admin.site.register(Book, BookAdmin)
admin.site.register(Author)
