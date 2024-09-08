from rest_framework import serializers
from .models import Author, Book
import datetime

# BookSerializer handles the serialization of Book model fields
# It includes custom validation for publication_year
class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['title', 'publication_year', 'author']

    # Custom validation to ensure the publication year is not in the future
    def validate_publication_year(self, value):
        if value > datetime.date.today().year:
            raise serializers.ValidationError("The publication year cannot be in the future.")
        return value

# AuthorSerializer includes a nested BookSerializer to serialize related books
# The 'books' field dynamically represents all books written by the author
class AuthorSerializer(serializers.ModelSerializer):
    # Nesting BookSerializer to handle related books
    books = BookSerializer(many=True, read_only=True)

    class Meta:
        model = Author
        fields = ['name', 'books']
