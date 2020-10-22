from django.urls import path
from .views import *

app_name = 'laundry'

urlpatterns = [
    # * Dashboard
    path('', laundry, name='laundry'),
    # * fetching sub_service from service while booking (ajax)
    path('sub_service/', sub_service, name='sub_service'),
    # * Customer Booking Details
    path('order/', Bookings, name='booking'),
    path('myorders/', Mybookings, name='mybooking'),
    path('myorders/<int:id>/', Booking_details, name='booking_details'),
    # * Customer Payment Details
    path('payments/', payment_list, name='payment'),
    # * Staff Booking Details
    path('staff_all_order/', staff_all_booking, name='staff_all_booking'),
    path('staff_all_order/<int:id>/edit',
         staff_booking_edit, name='staff_booking_edit'),
]
