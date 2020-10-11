from django.urls import path
from .views import *

app_name = 'staffmodule'

urlpatterns = [
    path('', staff_homepage, name="staff_homepage"),
    path('services', service_view, name="service"),
    path('services/<int:id>/edit/', service_edit, name="service_edit"),
    path('services/<int:id>/delete/', service_delete, name="service_delete"),
    path('list/', staff_list, name="staff_list"),
    path('<int:id>/detail/', staff_details, name="staff_details"),
]
