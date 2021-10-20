from django.contrib import admin

from web.models import Booking, Customer, Unit

admin.site.register(Unit)
admin.site.register(Customer)
admin.site.register(Booking)
