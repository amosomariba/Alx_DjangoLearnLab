from django.contrib import admin

from .models import CustomUser
from django.contrib.auth.admin import UserAdmin


@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    model = CustomUser
    fieldsets = UserAdmin.fieldsets + (
        (None, {"fields": ("bio", "profile_picture", "followers")}),
    )

# admin.site.register(CustomUser)
