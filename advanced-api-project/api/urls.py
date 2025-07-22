from django.urls import path, include
from .views import (
    BookListView,
    BookDetailView,
    BookCreateView,
    BookUpdateView,
    BookDeleteView,
)

urlpatterns = [
    path("books/", BookListView.as_view(), name="books-list"),
    path("books/<int:pk>/", BookDetailView.as_view(), name="books-detail"),
    path("books/create/", BookCreateView.as_view(), name="books-create"),
    path("books/update/<int:pk>/", BookUpdateView.as_view(), name="books-update"),
    path("books/delete/<int:pk>/", BookDeleteView.as_view(), name="books-delete"),
]
