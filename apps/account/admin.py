from django.contrib import admin
from .models import User


class UserAdmin(admin.ModelAdmin):
    list_display = ("email", "password", "username", "is_active")


admin.site.register(User, UserAdmin)
