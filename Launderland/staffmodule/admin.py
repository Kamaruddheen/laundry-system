from django.contrib import admin
from .models import Service


class ServiceAdmin(admin.ModelAdmin):
    list_display = ['id', 'service']
    search_fields = ['service']


admin.site.register(Service, ServiceAdmin)
