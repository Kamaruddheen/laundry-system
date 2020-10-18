from django.contrib import admin
from django.utils.translation import ugettext_lazy as _

from .models import Booking


class BookingAdmin(admin.ModelAdmin):
    fieldsets = (
        (_('User & Staff Details'), {'fields': ('cust_id', 'assigned_staff')}),
        (_('Laundry Details'), {
         'fields': ('services', 'unit')}),
        (_('Other Details'), {
            'fields': ('delivery_type', 'status', 'amount')}),
        (_('Important dates'), {'fields': ('delivered_on', )}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('cust_id', 'assigned_staff', 'services', 'unit', 'delivery_type', 'status', 'amount', 'booked_on', 'delivered_on'),
        }),
    )
    list_display = ['assigned_staff', 'delivery_type',
                    'status', 'booked_on', 'delivered_on']
    search_fields = ['service', 'assigned_staff', 'status']
    ordering = ('status',)


admin.site.register(Booking, BookingAdmin)
