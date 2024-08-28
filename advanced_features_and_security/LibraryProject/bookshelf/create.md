# Create a Book Instance

## Command:
```python
book = Book.objects.create(title="1984", author="George Orwell", publication_year=1949)


# The book instance is successfully created with the following details:
# book.id    # 1 (or another unique ID)
# book.title # "1984"
# book.author # "George Orwell"
# book.publication_year # 1949
