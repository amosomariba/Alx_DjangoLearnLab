from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=200)   # Field to store the title of the book
    author = models.CharField(max_length=200)  # Field to store the author's name

    def __str__(self):
        return self.title  # This method defines how the object is represented as a string
