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
BOOKING_STATUS_TO_SLUG = {choice[1]: choice[0] for choice in BOOKING_STATUS_CHOICES}
BOOKING_SLUG_TO_STATUS = {choice[0]: choice[1] for choice in BOOKING_STATUS_CHOICES}

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
    (RATE_PLAN_NON_REFUNDABLE, 'Non Refundable'),
    (RATE_PLAN_NON_REFUNDABLE_FAMILY, 'Non Refundable Family'),
)
RATE_PLAN_TO_SLUG = {choice[1]: choice[0] for choice in RATE_PLAN_CHOICES}
RATE_SLUG_TO_PLAN = {choice[0]: choice[1] for choice in RATE_PLAN_CHOICES}


# TODO: make into own model
UNIT_GROUP_SINGLE = 'single'
UNIT_GROUP_DOUBLE = 'double'
UNIT_GROUP_FAMILY = 'family'
UNIT_GROUP_CHOICES = (
    (UNIT_GROUP_SINGLE, 'Single'),
    (UNIT_GROUP_DOUBLE, 'Double'),
    (UNIT_GROUP_FAMILY, 'Family room'),
)
UNIT_GROUP_TO_SLUG = {choice[1]: choice[0] for choice in UNIT_GROUP_CHOICES}
UNIT_SLUG_TO_GROUP = {choice[1]: choice[0] for choice in UNIT_GROUP_CHOICES}


# TODO: make into own model
PROPERTY_CODE_BER = 'BER'
PROPERTY_CODE_LDN = 'LND'
PROPERTY_CODE_MUC = 'MUC'
PROPERTY_CODE_VIE = 'VIE'
PROPERTY_CODE_CHOICES = (
    (PROPERTY_CODE_BER, 'Berlin'),
    (PROPERTY_CODE_LDN, 'London'),
    (PROPERTY_CODE_MUC, 'Munich'),
    (PROPERTY_CODE_VIE, 'Vienna'),
)
PROPERTY_NAME_TO_CODE = {choice[1]: choice[0] for choice in PROPERTY_CODE_CHOICES}
PROPERTY_CODE_TO_NAME = {choice[0]: choice[1] for choice in PROPERTY_CODE_CHOICES}



class Customer(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    birth_date = models.DateField(null=True)
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

    def __str__(self):
        return f'{self.last_name}, {self.first_name}'


class Booking(models.Model):
    customer = models.ForeignKey('web.Customer', related_name="bookings", on_delete=models.CASCADE)
    unit = models.ForeignKey('web.Unit', related_name="bookings", on_delete=models.SET_NULL, null=True)
    property = models.ForeignKey('web.Property', related_name="bookings", on_delete=models.SET_NULL, null=True)
    adults = models.PositiveSmallIntegerField()
    children = models.PositiveSmallIntegerField()
    
    arrival = models.DateField()
    departure = models.DateField()
    checkin = models.DateTimeField(null=True)
    checkout = models.DateTimeField(null=True)
    
    rate_plan = models.CharField(max_length=30, choices=RATE_PLAN_CHOICES, default=RATE_PLAN_FLEXIBLE)
    status = models.CharField(max_length=20, choices=BOOKING_STATUS_CHOICES, default=BOOKING_STATUS_OPEN)

    travel_purpose = models.CharField(max_length=50)


class Unit(models.Model):
    unit = models.CharField(max_length=5, unique=True)
    unit_group = models.CharField(max_length=20, choices=UNIT_GROUP_CHOICES, default=UNIT_GROUP_DOUBLE)

    property = models.ForeignKey('web.Property', on_delete=models.CASCADE)

    class Meta:
        ordering = ('property', 'unit_group', 'unit')

    def __str__(self):
        return f'{self.unit} ({self.unit_group} / {self.property.name})'


class Property(models.Model):
    code = models.CharField(max_length=3)
    name = models.CharField(max_length=50)

    class Meta:
        ordering = ('code', )
        verbose_name_plural = 'properties'

    def __str__(self):
        return self.name
