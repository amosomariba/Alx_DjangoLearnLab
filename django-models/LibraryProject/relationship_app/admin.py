from django.contrib import admin
from .models import Author, Book, Librarian, Library


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ("name",)
    list_filter = ("name",)
    search_fields = ("name",)

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ("title", "author")
    list_filter = ("title", "author")
    search_fields = ("title", "author")
