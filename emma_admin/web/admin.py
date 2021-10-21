from django.contrib import admin

from web.models import Booking, Customer, Unit

class UnitAdmin(admin.ModelAdmin):
    list_display = ('unit', 'unit_group', 'property_code', )
    list_filter = ('unit_group', 'property_code', )

admin.site.register(Unit, UnitAdmin)

admin.site.register(Customer)
admin.site.register(Booking)
