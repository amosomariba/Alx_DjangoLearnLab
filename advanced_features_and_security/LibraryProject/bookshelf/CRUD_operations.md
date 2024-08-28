# Database Operations: CRUD in Django Shell

This document contains the commands used to perform CRUD operations on the `Book` model in the Django shell, along with their expected outputs.

```python
# Create a Book instance
book = Book.objects.create(title="1984", author="George Orwell", publication_year=1949)

# The book instance is successfully created with the following details:
# book.id               # 1 (or another unique ID)
# book.title            # "1984"
# book.author           # "George Orwell"
# book.publication_year # 1949

# Retrieve the created Book instance
retrieved_book = Book.objects.get(id=book.id)
print(retrieved_book.title)           # "1984"
print(retrieved_book.author)          # "George Orwell"
print(retrieved_book.publication_year) # 1949

# The book instance is retrieved with the following details:
# retrieved_book.title            # "1984"
# retrieved_book.author           # "George Orwell"
# retrieved_book.publication_year # 1949

# Update the title of the retrieved Book instance
retrieved_book.title = "Nineteen Eighty-Four"
retrieved_book.save()
print(retrieved_book.title) # "Nineteen Eighty-Four"

# The book title is successfully updated to:
# retrieved_book.title # "Nineteen Eighty-Four"

# Delete the Book instance
retrieved_book.delete()

# Try to retrieve all books to confirm deletion
all_books = Book.objects.all()
print(all_books) # <QuerySet []> (Empty QuerySet indicating no books are present)

# The book instance is successfully deleted, confirmed by an empty QuerySet:
# print(all_books) # <QuerySet []>
