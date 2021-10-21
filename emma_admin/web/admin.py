from django.contrib import admin

from web.models import PROPERTY_CODE_TO_NAME, Booking, Customer, Unit

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


class BookingAdmin(admin.ModelAdmin):
    list_display = (
        'customer', 
        'arrival', 'departure',
        'adults', 'children',
        'property',
        'status',
    )
    list_filter = (
        'arrival',
        'status',
        'unit',
    )

    #@admin.display(empty_value='???')
    def property(self, obj):
        return PROPERTY_CODE_TO_NAME[obj.unit.property_code]

admin.site.register(Booking, BookingAdmin)
