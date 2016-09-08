from django.contrib import admin

from adunits.models import Unit, Settings, Vendor


class UnitAdmin(admin.ModelAdmin):
    list_display = ['name', 'vendor', 'date_added']


admin.site.register(Unit, UnitAdmin)

admin.site.register(Settings)
admin.site.register(Vendor)
