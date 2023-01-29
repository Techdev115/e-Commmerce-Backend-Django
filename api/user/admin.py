from django.contrib import admin
from .models import CustomUser
from django.contrib.auth.models import AbstractUser

# Register your models here.

class UserAdmin(admin.ModelAdmin):
    exclude = ('user_permissions', 'groups', )
    ordering = ["created_at"]
    list_display = ["name", "email", "first_name", "last_name", "created_at", "last_login"]


admin.site.register(CustomUser, UserAdmin)
