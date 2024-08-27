# Import necessary models
from .models import Library, Author, Librarian, Book

# Fetch all books by a specific author
books = Book.objects.filter(author__name='Example')

# Fetch a specific library by name
library = Library.objects.get(name='library_name')

# Fetch all books in the specified library
library_books = Book.objects.filter(library=library)

# Fetch a specific author by name
author = Author.objects.get(name='author_name')

# Fetch all books by the specific author
author_books = Book.objects.filter(author=author)

# Fetch a librarian for a specific library
librarian = Librarian.objects.get(library=library)
