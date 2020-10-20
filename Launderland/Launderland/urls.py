from django.contrib import admin
from django.urls import path, include
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.auth import views as auth_views

from .views import *


urlpatterns = [
    path('', homepage, name="homepage"),
    path('serveradmin/', admin.site.urls),
    path('accounts/', include('usermodule.urls')),
    path('laundry/', include('laundry.urls')),
    path('staff/', include('staffmodule.urls')),
    path('customer/', include('customermodule.urls')),
    path('change_password_done/', auth_views.PasswordChangeDoneView.as_view(),
         name="password_change_done"),
]

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
