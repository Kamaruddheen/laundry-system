from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as DjangoUserAdmin
from django.utils.translation import ugettext_lazy as _

from .models import User


@admin.register(User)
class UserAdmin(DjangoUserAdmin):
    fieldsets = (
        (_('Login Details'), {'fields': ('mobile', 'password')}),
        (_('Personal Details'), {
         'fields': ('first_name', 'last_name', 'email', 'gender', 'profile_pic', 'user_type', 'staff_status')}),
        (_('Address Details'), {
            'fields': ('address', 'street', 'city', 'state', 'pincode')}),
        (_('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser',
                                       'groups', 'user_permissions')}),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('mobile', 'first_name', 'last_name', 'email', 'gender', 'profile_pic', 'user_type', 'password1', 'password2', 'address', 'street', 'city', 'state', 'pincode', 'staff_status'),
        }),
    )
    list_display = ('first_name', 'email', 'mobile',
                    'user_type', 'gender', 'is_staff')
    search_fields = ('email', 'first_name', 'last_name',
                     'mobile', 'pincode', 'gender')
    ordering = ('user_type', 'first_name')
