from django.contrib import admin

# Register your models here.
from .models import CarTransport,NavalTransport,TransportType,Car_routes,Naval_routes


class CarTransportAdmin(admin.ModelAdmin):
    pass

class NavalTransportAdmin(admin.ModelAdmin):
    pass

class TransportTypeAdmin(admin.ModelAdmin):
    pass


class Car_routesAdmin(admin.ModelAdmin):
    pass

class Naval_routesAdmin(admin.ModelAdmin):
    pass

admin.site.register(CarTransport, CarTransportAdmin)
admin.site.register(NavalTransport, NavalTransportAdmin)
admin.site.register(TransportType, TransportTypeAdmin)
admin.site.register(Car_routes, Car_routesAdmin)
admin.site.register(Naval_routes, Naval_routesAdmin)