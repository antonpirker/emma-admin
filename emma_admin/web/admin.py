import json
from django.contrib import admin
from django.core.serializers.json import DjangoJSONEncoder
from django.db.models import Sum
from django.db.models.functions import TruncDay

from web.models import PROPERTY_CODE_TO_NAME, Booking, Customer, Unit, Property


@admin.register(Property)
class PropertyAdmin(admin.ModelAdmin):
    list_display = ('name', 'code', )


@admin.register(Unit)
class UnitAdmin(admin.ModelAdmin):
    list_display = ('unit', 'unit_group', 'property', )
    list_filter = ('unit_group', 'property', )


@admin.register(Customer)
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


@admin.register(Booking)
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
        'property',
    )
    ordering = ('-arrival', )

    def changelist_view(self, request, extra_context=None):
        response = super(BookingAdmin, self).changelist_view(request, extra_context)
        filtered_query_set = response.context_data["cl"].queryset
        # Aggregate new subscribers per day
        chart_data = (
            filtered_query_set.annotate(date=TruncDay("arrival"))
            .values("date")
            .annotate(y=Sum("adults"))
            .order_by("-arrival")
        )

        # Serialize and attach the chart data to the template context
        as_json = json.dumps(list(chart_data), cls=DjangoJSONEncoder)
        extra_context = {
            "chart_data": as_json
        }
        response.context_data.update(extra_context)

        return response