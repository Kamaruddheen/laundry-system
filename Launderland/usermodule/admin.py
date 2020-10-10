from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as DjangoUserAdmin
from django.utils.translation import ugettext_lazy as _

from .models import User


@admin.register(User)
class UserAdmin(DjangoUserAdmin):
    fieldsets = (
        (None, {'fields': ('mobile', 'password')}),
        (_('Personal info'), {
         'fields': ('first_name', 'last_name', 'email', 'profile_pic', 'user_type')}),
        (_('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser',
                                       'groups', 'user_permissions')}),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('mobile', 'first_name', 'last_name', 'email', 'user_type', 'password1', 'password2'),
        }),
    )
    list_display = ('first_name', 'email', 'mobile', 'is_staff')
    search_fields = ('email', 'first_name', 'last_name', 'mobile')
    ordering = ('email',)
