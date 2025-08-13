from rest_framework import serializers
from .models import TransportType ,Route

class TransportTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = TransportType
        fields = '__all__'


class RoutesTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model=Route
        fields='__all__'