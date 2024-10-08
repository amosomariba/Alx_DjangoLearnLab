from django.urls import path
from django.contrib.auth import views as auth_views
from .views import list_books, LibraryDetailView
from .views import register
from . import views

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name='relationship_app/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='relationship_app/logout.html'), name='logout'),
    path('register/', views.register, name='register'),
    path('books/', list_books, name='list_books'),
    path('library/<int:pk>/', LibraryDetailView.as_view(), name='library_detail'),
    path('admin/', views.admin_view, name='admin_view'),
    path('librarian/', views.librarian_view, name='librarian_view'),
    path('member/', views.member_view, name='member_view')
    path('add_book/', views.BookCreateView.as_view(), name='add_book'),
    path('edit_book/<int:pk>/edit/', views.BookUpdateView.as_view(), name='edit_book'),
    path('delete_book/<int:pk>/delete/', views.BookDeleteView.as_view(), name='delete_book')
]
