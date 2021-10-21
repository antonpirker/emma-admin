from django.contrib import admin

from web.models import Booking, Customer, Unit

class UnitAdmin(admin.ModelAdmin):
    list_display = ('unit', 'unit_group', 'property_code', )
    list_filter = ('unit_group', 'property_code', )

admin.site.register(Unit, UnitAdmin)

class CustomerAdmin(admin.ModelAdmin):
    list_display = (
        'last_name', 'first_name', 'birth_date',
        'nationality', 'country_code', 'city',
        'phone', 'email',
        'comment', 'customer_comment',
        )
    list_filter = (
        'nationality', 'country_code', 'city', 'preferred_language',
    )
    fieldsets = (
        (None, {
            'fields': (
                'last_name', 'first_name', 'birth_date', 'nationality',
            )
        }),
        ('Contact', {
            'fields': (
                'email', 'phone', 'preferred_language',
            )
        }),

        ('Address', {
            'fields': (
                'address_line_1', 'address_line_2', 'postal_code', 'city',
                'country_code',
            )
        }),
        ('Comments', {
            'fields': (
                'comment', 'customer_comment',
            ),
        }),
    )


admin.site.register(Customer, CustomerAdmin)


admin.site.register(Booking)
