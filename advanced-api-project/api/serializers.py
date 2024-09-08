from rest_framework import serializers
from .models import Author, Book
import datetime

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['title', 'publication_year', 'author']

    # Custom validation to ensure the publication year is not in the future
    def validate_publication_year(self, value):
        if value > datetime.date.today().year:
            raise serializers.ValidationError("The publication year cannot be in the future.")
        return value

class AuthorSerializer(serializers.ModelSerializer):
    # Nesting BookSerializer to handle related books
    books = BookSerializer(many=True, read_only=True)

    class Meta:
        model = Author
        fields = ['name', 'books']
