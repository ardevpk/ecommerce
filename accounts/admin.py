from django.contrib import admin
from django.contrib.auth import get_user_model
from .models import *
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
# User = get_user_model()


class UserAdmin(BaseUserAdmin):
    list_display = ["username", "email", "is_verified"]
    fieldsets = BaseUserAdmin.fieldsets
    fieldsets[0][-1]['fields'] = fieldsets[0][-1]['fields'] + (
        'is_verified',
    )

admin.site.register(User, UserAdmin)
# Register your models here.
