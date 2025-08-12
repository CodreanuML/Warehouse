from rest_framework import serializers
from .models import TransportType

class TransportTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = TransportType
        fields = '__all__'