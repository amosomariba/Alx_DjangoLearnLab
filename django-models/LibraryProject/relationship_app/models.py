from django.db import models


# Author Model
class Author(models.Model):
    name = models.CharField(max_length=100)  # CharField for the author's name

    def __str__(self):
        return self.name


# Book Model
class Book(models.Model):
    title = models.CharField(max_length=200)  # CharField for the book's title
    author = models.ForeignKey(Author, on_delete=models.CASCADE)  # ForeignKey to Author

    def __str__(self):
        return self.title


# Library Model
class Library(models.Model):
    name = models.CharField(max_length=100)  # CharField for the library's name
    books = models.ManyToManyField(Book)  # ManyToManyField to Book

    def __str__(self):
        return self.name


# Librarian Model
class Librarian(models.Model):
    name = models.CharField(max_length=100)  # CharField for the librarian's name
    library = models.OneToOneField(
        Library, on_delete=models.CASCADE
    )  # OneToOneField to Library

    def __str__(self):
        return self.name
