
### 2. `retrieve.md`
**Title**: Retrieve the Book Instance

```markdown
# Retrieve the Book Instance

## Command:
```python
retrieved_book = Book.objects.get(id=book.id)
print(retrieved_book.title)           # "1984"
print(retrieved_book.author)          # "George Orwell"
print(retrieved_book.publication_year) # 1949


# The book instance is retrieved with the following details:
# retrieved_book.title           # "1984"
# retrieved_book.author          # "George Orwell"
# retrieved_book.publication_year # 1949

