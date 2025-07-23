from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    bio = models.TextField(
        max_length=500,
        blank=True,
        null=True,
        help_text="Tell us about yourself here (max 500 characters)",
    )
    profile_picture = models.ImageField(
        upload_to="profile_pics/",
        blank=True,
        null=True,
        default="profile_pics/default.jpg",
        help_text="Upload your picture",
    )
    followers = models.ManyToManyField(
        "self", symmetrical=False, related_name="following", blank=True
    )
    profile_updated=models.DateTimeField(auto_now=True)
    is_verified=models.BooleanField(default=False)

    class Meta:
        verbose_name = "User"
        verbose_name_plural = "Users"

    def __str__(self):
        return f"@{self.username}"

    def get_followers_count(self):
        return self.followers.count()

    def get_following_count(self):
        """
        Method to get the number of users this user is following
        """
        return self.following.count()

    def is_following(self, user):
        """
        Check if this user is following another user
        Returns True if following, False if not
        """
        return self.following.filter(id=user.id).exists()

    def follow(self, user):
        """
        Method to follow another user
        """
        if not self.is_following(user) and user != self:
            self.following.add(user)

    def unfollow(self, user):
        """
        Method to unfollow another user
        """
        if self.is_following(user):
            self.following.remove(user)
