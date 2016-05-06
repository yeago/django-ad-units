from django.contrib import admin

from adunits.models import Unit, Settings


class UnitAdmin(admin.ModelAdmin):
    list_display = ['name', 'date_added']


admin.site.register(Unit, UnitAdmin)

admin.site.register(Settings)
