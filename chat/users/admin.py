from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import User

class UserAdmin(BaseUserAdmin):
    def save_model(self, request, obj, form, change):
        if not change:
            password = obj.email[::2]
            obj.set_password(password)
        super().save_model(request, obj, form, change)

admin.site.register(User, UserAdmin)