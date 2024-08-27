from relationship_app.models import Author, Book, Library, Librarian

def query_books_by_author(author_name):
    author = Author.objects.get(name=author_name)
    books = Book.objects.filter(author=author)
    return books

def list_books_in_library(library_name):
    library = Library.objects.get(name=library_name)
    return library.books.all()

def get_librarian_for_library(library_name):
    library = Library.objects.get(name=library_name)
    return Librarian.objects.get(library=library)

# Example usage:
if __name__ == "__main__":
    # Assuming you've already created some sample data
    author_books = query_books_by_author("J.K. Rowling")
    print("Books by J.K. Rowling:", [book.title for book in author_books])

    library_books = list_books_in_library("New York Public Library")
    print("Books in New York Public Library:", [book.title for book in library_books])

    librarian = get_librarian_for_library("New York Public Library")
    print("Librarian of New York Public Library:", librarian.name)