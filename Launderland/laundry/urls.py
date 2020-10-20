from django.urls import path
from .views import *

app_name = 'laundry'

urlpatterns = [
    # * Dashboard
    path('', laundry, name='laundry'),
    # * fetching sub_service from service while booking (ajax)
    path('sub_service/', sub_service, name='sub_service'),
    # * Customer Booking Details
    path('booking/', Bookings, name='booking'),
    path('mybookings/', Mybookings, name='mybooking'),
    path('mybookings/<int:id>/', Booking_details, name='booking_details'),
    # * Staff Booking Details
    path('staff_all_booking/', staff_all_booking, name='staff_all_booking'),
    path('staff_all_booking/<int:id>/edit',
         staff_booking_edit, name='staff_booking_edit'),
]
