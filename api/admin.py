from django.contrib import admin
from .models import User
from django.contrib.auth.admin import UserAdmin
from .forms import *


class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = User
    list_display = ['username', 'email', 'first_name',
                    'last_name', 'is_staff',]
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('avatar',)}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {'fields': ('avatar',)}),
    )


admin.site.register(User, CustomUserAdmin)
