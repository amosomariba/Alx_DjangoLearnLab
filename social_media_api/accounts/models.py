# accounts/models.py
from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models

class CustomUser(AbstractUser):
    following = models.ManyToManyField(
        'self',
        symmetrical=False,
        related_name='followers',
        blank=True,
        through='CustomUserFollowing'
    )
    
    groups = models.ManyToManyField(
        Group,
        related_name="customuser_set",
        blank=True,
        help_text="The groups this user belongs to.",
        verbose_name="groups",
        related_query_name="user",
    )
    
    user_permissions = models.ManyToManyField(
        Permission,
        related_name="customuser_set",
        blank=True,
        help_text="Specific permissions for this user.",
        verbose_name="user permissions",
        related_query_name="user",
    )

    def __str__(self):
        return self.username

class CustomUserFollowing(models.Model):
    from_user = models.ForeignKey(CustomUser, related_name='following_relationships', on_delete=models.CASCADE)
    to_user = models.ForeignKey(CustomUser, related_name='followed_by_relationships', on_delete=models.CASCADE)

    class Meta:
        unique_together = ('from_user', 'to_user')
