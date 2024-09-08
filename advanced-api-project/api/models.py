from django.db import models

# Author model represents book authors
# Each author can have multiple books (one-to-many relationship)
class Author(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


# Book model represents individual books
# Each book is linked to an author via a ForeignKey
class Book(models.Model):
    title = models.CharField(max_length=255)
    publication_year = models.IntegerField()
    author = models.ForeignKey(Author, related_name='books', on_delete=models.CASCADE)

    def __str__(self):
        return self.title
