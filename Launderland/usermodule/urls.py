from django.urls import path
from .views import *

app_name = 'usermodule'

urlpatterns = [
    path('signup/', customer_signup, name='signup'),
    path('signin/', account_signin, name='signin'),
    path('signout/', account_signout, name='signout'),
    path('myaccount/', account_profile, name='myaccount'),
    path('staff/signup/', staff_signup, name='signup_staff'),
]
