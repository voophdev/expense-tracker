from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from authentication.models import Users


class CustomUserAdmin(UserAdmin):
    model = Users
    list_display = ['id', 'username','email', 'first_name', 'last_name', 
                    'address','mobile_number', 'is_staff', 'is_active']
    search_fields = ['email', 'first_name', 'last_name']
    ordering = ['email']
    fieldsets = (
        (None, {'fields': ('email', 'username', 'password')}),
        ('Personal info', {'fields': ('first_name', 'last_name', 'address', 'mobile_number')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': (
                'email', 'password1', 'password2', 
                'address', 'mobile_number', 
                'is_active', 'is_staff', 'is_superuser', 
                'groups', 'user_permissions'
            ),
        }),
    )
    form = UserChangeForm
    add_form = UserCreationForm


admin.site.register(Users, CustomUserAdmin)