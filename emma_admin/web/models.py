from django.db import models
from django.db.models.fields import EmailField
from django.db.models.query_utils import check_rel_lookup_compatibility


# TODO: make into own model
BOOKING_STATUS_OPEN = 'open'
BOOKING_STATUS_PENDING = 'pending'
BOOKING_STATUS_CONFIRMED = 'confirmed'
BOOKING_STATUS_CHOICES = (
    (BOOKING_STATUS_OPEN, 'Open'),
    (BOOKING_STATUS_PENDING, 'Pending'),
    (BOOKING_STATUS_CONFIRMED, 'Confirmed'),
)


# TODO: make into own model
RATE_PLAN_FLEXIBLE = 'flexible'
RATE_PLAN_FLEXIBLE_FAMILY = 'flexible-family'
RATE_PLAN_INCLUDE_BREAKFAST = 'include-breakfast'
RATE_PLAN_NON_REFUNDABLE = 'non-refundable'
RATE_PLAN_NON_REFUNDABLE_FAMILY = 'non-refundable-family'
RATE_PLAN_CHOICES = (
    (RATE_PLAN_FLEXIBLE, 'Flexible'),
    (RATE_PLAN_FLEXIBLE_FAMILY, 'Flexible Family'),
    (RATE_PLAN_INCLUDE_BREAKFAST, 'Include Breakfast'),
    (RATE_PLAN_NON_REFUNDABLE, 'None Refundable'),
    (RATE_PLAN_NON_REFUNDABLE_FAMILY, 'Non Refundable Family'),
)


# TODO: make into own model
UNIT_GROUP_SINGLE = 'single'
UNIT_GROUP_DOUBLE = 'double'
UNIT_GROUP_FAMILY = 'family'
UNIT_GROUP_CHOICES = (
    (UNIT_GROUP_SINGLE, 'Single'),
    (UNIT_GROUP_DOUBLE, 'Double'),
    (UNIT_GROUP_FAMILY, 'Family room'),
)


# TODO: make into own model
PROPERTY_CODE_BER = 'BER'
PROPERTY_CODE_LDN = 'LDN'
PROPERTY_CODE_MUC = 'MUC'
PROPERTY_CODE_VIE = 'VIE'
PROPERTY_CODE_CHOICES = (
    (PROPERTY_CODE_BER, 'Berlin'),
    (PROPERTY_CODE_LDN, 'London'),
    (PROPERTY_CODE_MUC, 'Munich'),
    (PROPERTY_CODE_VIE, 'Vienna'),
)


class Customer(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    birth_date = models.DateField()
    nationality = models.CharField(max_length=2) # ISO 3166
    preferred_language = models.CharField(max_length=2, default='en') # ISO 639-1
    address_line_1 = models.CharField(max_length=50)
    address_line_2 = models.CharField(max_length=50)
    postal_code = models.CharField(max_length=20)
    city = models.CharField(max_length=50)
    country_code = models.CharField(max_length=2)
    email = models.EmailField()
    phone = models.CharField(max_length=50)
    comment = models.TextField()
    customer_comment = models.TextField()

    class Meta:
        ordering = ('last_name', 'first_name')


class Booking(models.Model):
    customer = models.ForeignKey('web.Customer', related_name="bookings", on_delete=models.CASCADE)
    unit = models.ForeignKey('web.Unit', related_name="bookings", on_delete=models.SET_NULL, null=True)
    adults = models.PositiveSmallIntegerField()
    children = models.PositiveSmallIntegerField()
    
    arrival = models.DateField()
    departure = models.DateField()
    checkin = models.DateTimeField()
    checkout = models.DateTimeField()
    
    rate_plan = models.CharField(max_length=30, choices=RATE_PLAN_CHOICES, default=RATE_PLAN_FLEXIBLE)
    status = models.CharField(max_length=20, choices=BOOKING_STATUS_CHOICES, default=BOOKING_STATUS_OPEN)

    travel_purpose = models.CharField(max_length=50)

  

class Unit(models.Model):
    property_code = models.CharField(max_length=3, choices=PROPERTY_CODE_CHOICES, default=PROPERTY_CODE_VIE)
    unit_group = models.CharField(max_length=20, choices=UNIT_GROUP_CHOICES, default=UNIT_GROUP_DOUBLE)
    unit = models.CharField(max_length=5)

    class Meta:
        ordering = ('property_code', 'unit_group', 'unit')

