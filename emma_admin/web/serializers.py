from rest_framework import serializers

from web.models import Booking, Customer, Unit, Property


class CustomerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Customer
        fields = [
            'last_name', 'first_name', 'birth_date',
            'nationality', 'preferred_language', 
            'address_line_1', 'address_line_2', 
            'postal_code', 'city', 'country_code', 
            'email', 'phone',
            'comment', 'customer_comment',
        ]


class UnitSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Unit
        fields = [
            'property', 'unit_group', 'unit',
        ]


class PropertySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Property
        fields = [
            'code', 'name',
        ]


class BookingSerializer(serializers.ModelSerializer):
    customer = CustomerSerializer()
    unit = UnitSerializer()
    property = PropertySerializer()
    
    class Meta:
        model = Booking
        fields = [
            'customer', 'unit', 'property',
            'adults', 'children', 
            'arrival', 'departure',
            'rate_plan', 'status', 'travel_purpose',
        ]