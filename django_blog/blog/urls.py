from django.urls import path
from .views import register, profile
from django.contrib.auth.views import LoginView, LogoutView
from .views import PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView
from .views import CommentCreateView, CommentUpdateView, CommentDeleteView

# urlpatterns = [
#     path('login/', LoginView.as_view(template_name='blog/login.html'), name='login'),
#     path('logout/', LogoutView.as_view(template_name='blog/logout.html'), name='logout'),
#     path('register/', register, name='register'),
#     path('profile/', profile, name='profile'),
#     path('', PostListView.as_view(), name='post-list'),  # List all posts
#     path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),  # View a post in detail
#     path('post/new/', PostCreateView.as_view(), name='post-create'),  # Create a new post
#     path('post/<int:pk>/edit/', PostUpdateView.as_view(), name='post-update'),  # Edit (update) a post
#     path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),  # Delete a post
#     ["post/<int:pk>/update/"]
#     path('post/<int:pk>/comment/', CommentCreateView.as_view(), name='comment-create'),
#     path('comment/<int:pk>/edit/', CommentUpdateView.as_view(), name='comment-update'),
#     path('comment/<int:pk>/delete/', CommentDeleteView.as_view(), name='comment-delete'),
# ]

from django.urls import path
from .views import register, profile
from django.contrib.auth.views import LoginView, LogoutView
from .views import PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView
from .views import CommentCreateView, CommentUpdateView, CommentDeleteView
from .views import PostByTagListView

urlpatterns = [
    path('login/', LoginView.as_view(template_name='blog/login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='blog/logout.html'), name='logout'),
    path('register/', register, name='register'),
    path('profile/', profile, name='profile'),
    
    # Post URLs
    path('', PostListView.as_view(), name='post-list'),  # List all posts
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),  # View a post in detail
    path('post/new/', PostCreateView.as_view(), name='post-create'),  # Create a new post
    path('post/<int:pk>/edit/', PostUpdateView.as_view(), name='post-update'),  # Edit (update) a post
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),  # Delete a post

    # Comment URLs
    path('post/<int:pk>/comments/new/', CommentCreateView.as_view(), name='comment-create'),  # Create a new comment
    path('comment/<int:pk>/update/', CommentUpdateView.as_view(), name='comment-update'),  # Edit (update) a comment
    path('comment/<int:pk>/delete/', CommentDeleteView.as_view(), name='comment-delete'),  # Delete a comment
    
    # Other URL patterns
    path('tags/<slug:tag_slug>/', PostByTagListView.as_view(), name='post_by_tag'),
]




