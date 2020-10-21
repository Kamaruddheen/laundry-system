from django.urls import path
from .views import *

app_name = 'staffmodule'

urlpatterns = [
    #  ? SERVICES
    path('services/', service_view, name="service"),
    path('services/<int:id>/edit/', service_edit, name="service_edit"),
    path('services/<int:id>/delete/', service_delete, name="service_delete"),
    #  ? SUBSERVICES
    path('services/<int:id>/subservices/',
         sub_service_view, name="subservices"),
    path('subservices/<int:id>/edit/',
         sub_service_edit, name="sub_service_edit"),
    path('subservices/<int:id>/delete/',
         sub_service_delete, name="sub_service_delete"),
    #  ? STAFF
    path('list/', staff_list, name="staff_list"),
    path('<int:id>/detail/', staff_details, name="staff_details"),
]
