from django.db import models
from django.core.exceptions import ValidationError

class Transport(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class TransportType(models.Model):
    CATEGORY_CHOICES = [
        ('cargo', 'Cargo'),
        ('personnel', 'Personnel'),
        ('military', 'Military'),
    ]

    UNIT_CHOICES = [
        ('kg', 'Kilograms'),
        ('pers', 'Persons'),
        ('units', 'Units'),
    ]

    name = models.CharField(max_length=50)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    capacity = models.IntegerField(default=0)
    capacity_unit = models.CharField(max_length=10, choices=UNIT_CHOICES, blank=True)

    @staticmethod
    def get():
        return [(obj.name, obj.name) for obj in TransportType.objects.all()]

    def __str__(self):
        return f"{self.name} ({self.category}) - {self.capacity} {self.capacity_unit}"


class Route(models.Model):
    ROUTE_TYPE_CHOICES = [
        ('land', 'Land'),
        ('naval', 'Naval'),
        ('air', 'Air'),
    ]

    route_type = models.CharField(max_length=10, choices=ROUTE_TYPE_CHOICES)
    from_T = models.CharField(max_length=50)
    to_T = models.CharField(max_length=50)
    name = models.CharField(max_length=100, null=True, blank=True)
    length = models.IntegerField(default=0)

    @staticmethod
    def get():
        return [(obj.name, obj.name) for obj in Route.objects.all()]

    def save(self, *args, **kwargs):
        self.name = f"{self.from_T}-{self.to_T}"
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.name} ({self.get_route_type_display()})"


class LandTransport(Transport):
    transport_type = models.ForeignKey(TransportType, on_delete=models.CASCADE,null=True, blank=True)
    available = models.BooleanField()
    route = models.ForeignKey(Route, on_delete=models.CASCADE,null=True, blank=True)

    def clean(self):
        if self.route and self.route.route_type != 'land':
            raise ValidationError("Only land routes can be assigned to LandTransport.")


class NavalTransport(Transport):
    transport_type = models.ForeignKey(TransportType, on_delete=models.CASCADE,null=True, blank=True)
    available = models.BooleanField()
    route = models.ForeignKey(Route, on_delete=models.CASCADE,null=True, blank=True)

    def clean(self):
        if self.route and self.route.route_type != 'naval':
            raise ValidationError("Only naval routes can be assigned to NavalTransport.")


class AirTransport(Transport):
    transport_type = models.ForeignKey(TransportType, on_delete=models.CASCADE,null=True, blank=True)
    available = models.BooleanField()
    route = models.ForeignKey(Route, on_delete=models.CASCADE,null=True, blank=True)

    def clean(self):
        if self.route and self.route.route_type != 'air':
            raise ValidationError("Only air routes can be assigned to AirTransport.")