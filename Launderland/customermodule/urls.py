from django.urls import path
from .views import *

app_name = 'customermodule'

urlpatterns = [
    path('list/', customer_list, name="customer_list"),
    path('<int:id>/detail/', customer_details, name="customer_details"),
]
