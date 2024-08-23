from django.contrib import admin
from .models import Book

# Register your models here.
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'publication_year')  # Display title, author, and publication_year in the list view
    search_fields = ('title', 'author')  # Enable search by title and author
    list_filter = ('publication_year',)  # Add a filter for publication_year

# Register the Book model with the BookAdmin configuration
admin.site.register(Book, BookAdmin)