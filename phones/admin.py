from django.contrib import admin
from .models import Manufacturer, Phone


class PhoneAdmin(admin.ModelAdmin):
    list_display = ('manufacturer', 'model', 'operating_system', 'color', 'price', 'delivery')
    fields = ('manufacturer', 'model', 'operating_system', 'color', 'release_year', 'memory', ('price', 'delivery'))
    search_fields = ('model',)


admin.site.register(Manufacturer)
admin.site.register(Phone, PhoneAdmin)
