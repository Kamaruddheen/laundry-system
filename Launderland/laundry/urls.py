from django.urls import path
from .views import *

app_name = 'laundry'

urlpatterns = [
    path('', laundry, name='laundry'),
    path('sub_service/', sub_service, name='sub_service'),
    path('booking/', Bookings, name='booking'),
    path('mybookings/', Mybookings, name='mybooking'),
    path('mybookings/<int:id>/', Booking_details, name='booking_details'),
    path('staff_all_booking/', staff_all_booking, name='staff_all_booking'),
    path('staff_all_booking/<int:id>/edit',
         staff_booking_edit, name='staff_booking_edit'),
]
