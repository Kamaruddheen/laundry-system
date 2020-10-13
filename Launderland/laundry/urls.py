from django.urls import path
from .views import *

app_name = 'laundry'

urlpatterns = [
    path('', laundry, name='laundry'),
    path('booking/', Bookings, name='booking'),
]
