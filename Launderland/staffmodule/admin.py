from django.contrib import admin
from .models import Service, Subservice


class ServiceAdmin(admin.ModelAdmin):
    list_display = ['service', 'id']
    search_fields = ['service']


admin.site.register(Service, ServiceAdmin)


class SubserviceAdmin(admin.ModelAdmin):
    list_display = ['sub_service', 'service', 'id']
    search_fields = ['service', 'sub_service']


admin.site.register(Subservice, SubserviceAdmin)
