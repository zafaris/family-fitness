from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserChangeForm, CustomUserCreationForm
from .models import User


# Register your models here.
class CustomUserAdmin(UserAdmin):
    model = User
    form = CustomUserChangeForm
    add_form = CustomUserCreationForm
    list_display = ('email', 'name')
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('name',)}),
    )

admin.site.register(User, CustomUserAdmin)
