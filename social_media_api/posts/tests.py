from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from django.contrib.auth import get_user_model
from .models import Post, Like


class LikePostTests(APITestCase):
    def setUp(self):
        # Create test users
        self.user1 = User.objects.create_user(username='user1', password='password123')
        self.user2 = User.objects.create_user(username='user2', password='password123')

        # Create a test post
        self.post = Post.objects.create(
            title='Test Post',
            content='This is a test post.',
            author=self.user1
        )

        # Authenticate user1
        self.client.login(username='user1', password='password123')

    def test_like_post(self):
        response = self.client.post(reverse('like-post', args=[self.post.pk]))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_unlike_post(self):
        self.client.post(reverse('like-post', args=[self.post.pk]))
        response = self.client.post(reverse('unlike-post', args=[self.post.pk]))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

