from django.urls import path
from .views import *

app_name = 'staffmodule'

urlpatterns = [
    path('', staff_homepage, name='staff_homepage'),
    path('services', service, name='service'),
    path('services/<int:id>/edit/', service_edit, name="service_edit"),
    path('services/<int:id>/delete/', service_delete, name="service_delete"),
]
