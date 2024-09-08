from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from rest_framework.exceptions import ValidationError
from .models import Book
from django.contrib.auth.models import User

class BookTests(APITestCase):
    def setUp(self):
        # Create a test user and authenticate
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.client.login(username='testuser', password='testpassword')

        # Create a test book
        self.book = Book.objects.create(
            title='Test Book',
            author='Test Author',
            publication_year=2024
        )
        self.url = reverse('book-list')  # Adjust according to your URL configuration

    def test_create_book(self):
        data = {
            'title': 'New Book',
            'author': 'New Author',
            'publication_year': 2023
        }
        response = self.client.post(self.url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Book.objects.count(), 2)  # Verify book count increased
        self.assertEqual(Book.objects.latest('id').title, 'New Book')  # Verify book details

    def test_update_book(self):
        url = reverse('book-detail', kwargs={'pk': self.book.pk})
        data = {'title': 'Updated Title'}
        response = self.client.patch(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.book.refresh_from_db()
        self.assertEqual(self.book.title, 'Updated Title')

    def test_delete_book(self):
        url = reverse('book-detail', kwargs={'pk': self.book.pk})
        response = self.client.delete(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Book.objects.count(), 0)  # Verify book was deleted

    def test_filter_books(self):
        url = f"{self.url}?title=Test Book"
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data['results']), 1)  # Verify the correct number of filtered books

    def test_search_books(self):
        url = f"{self.url}?search=Test Book"
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data['results']), 1)  # Verify search results

    def test_order_books(self):
        url = f"{self.url}?ordering=title"
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        # Verify ordering by title (you might need to add more detailed checks based on your data)

    def test_permissions(self):
        # Test non-authenticated access
        self.client.logout()
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
