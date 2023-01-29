from django.contrib import admin
from .models import Product



class UserAdmin(admin.ModelAdmin):
    # search_fields = ["name", "category"]
    ordering = ["created_at"]
    list_display = ["name", "price", "stock", "category", "created_at"]


admin.site.register(Product, UserAdmin)
