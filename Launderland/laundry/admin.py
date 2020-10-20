from django.contrib import admin
from django.utils.translation import ugettext_lazy as _

from .models import *


class BookingAdmin(admin.ModelAdmin):
    fieldsets = (
        (_('User & Staff Details'), {'fields': ('cust_id', 'assigned_staff')}),
        (_('Laundry Details'), {
         'fields': ('services', 'sub_service', 'quantity')}),
        (_('Other Details'), {
            'fields': ('delivery_type', 'status', 'amount')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('cust_id', 'assigned_staff', 'services', 'sub_service', 'quantity', 'delivery_type', 'status', 'amount', 'booked_on'),
        }),
    )
    list_display = ['assigned_staff', 'delivery_type',
                    'status', 'booked_on']
    search_fields = ['service', 'assigned_staff', 'status']
    ordering = ('-status',)


admin.site.register(Booking, BookingAdmin)


class PaymentAdmin(admin.ModelAdmin):
    fieldsets = (
        (_('User & Booking Details'), {
         'fields': ('cust_id', 'booking_id')}),
        (_('Payment Details'), {
         'fields': ('payment_mode', 'paid_amount', 'status')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('cust_id', 'booking_id', 'payment_mode', 'paid_date', 'paid_amount', 'status'),
        }),
    )
    list_display = ['cust_id', 'paid_amount', 'paid_date', 'status']
    search_fields = ['status', 'paid_date', 'cust_id', 'booking_id']
    ordering = ('-status',)


admin.site.register(Payment, PaymentAdmin)
