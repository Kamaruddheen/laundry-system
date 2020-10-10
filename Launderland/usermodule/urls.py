from django.urls import path
from .views import *

app_name = 'usermodule'

urlpatterns = [
    path('signup/', customer_signup, name='signup'),
    path('signin/', account_signin, name='signin'),
    path('signout/', customer_signout, name='signout'),
    path('myaccount/', customer_profile, name='myaccount'),
]
