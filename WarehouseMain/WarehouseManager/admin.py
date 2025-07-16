from django.contrib import admin
from .models import (
    Transport,
    TransportType,
    Route,
    LandTransport,
    NavalTransport,
    AirTransport,
)

# Înregistrare model de bază Transport (dacă vrei să îl vezi separat în admin)
@admin.register(Transport)
class TransportAdmin(admin.ModelAdmin):
    list_display = ("id", "name")
    search_fields = ("name",)

# Admin pentru TransportType
@admin.register(TransportType)
class TransportTypeAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "category", "capacity", "capacity_unit")
    list_filter = ("category",)
    search_fields = ("name",)
    ordering = ("name",)

# Admin pentru Route
@admin.register(Route)
class RouteAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "route_type", "from_T", "to_T", "length")
    list_filter = ("route_type",)
    search_fields = ("name", "from_T", "to_T")
    ordering = ("name",)

# Admin pentru LandTransport
@admin.register(LandTransport)
class LandTransportAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "transport_type", "available", "route")
    list_filter = ("available", "transport_type")
    search_fields = ("name",)
    ordering = ("name",)

# Admin pentru NavalTransport
@admin.register(NavalTransport)
class NavalTransportAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "transport_type", "available", "route")
    list_filter = ("available", "transport_type")
    search_fields = ("name",)
    ordering = ("name",)

# Admin pentru AirTransport
@admin.register(AirTransport)
class AirTransportAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "transport_type", "available", "route")
    list_filter = ("available", "transport_type")
    search_fields = ("name",)
    ordering = ("name",)