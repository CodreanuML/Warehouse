from django.forms import ModelForm
from .models import Transport, TransportType, Route, LandTransport, NavalTransport, AirTransport

class TransportTypeForm(ModelForm):
	class Meta:
		model = TransportType
		fields = ["name", "category", "capacity", "capacity_unit"]


class RouteForm(ModelForm):
	class Meta:
		model = Route
		fields = ["route_type", "from_T", "to_T","length"]	


class LandTransportForm(ModelForm):
	class Meta:
		model = LandTransport
		fields = ["transport_type", "available", "route"]	


class NavalTransportForm(ModelForm):
	class Meta:
		model = NavalTransport
		fields = ["transport_type", "available", "route"]	


class AirTransportForm(ModelForm):
	class Meta:
		model = AirTransport
		fields = ["transport_type", "available", "route"]	