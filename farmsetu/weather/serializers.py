from .models import Weather
from rest_framework import serializers


class WeatherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Weather
        fields = '__all__'


class ClimateSerializer(serializers.Serializer):
    order_by = serializers.CharField(max_length=28)
    region = serializers.CharField(max_length=28)
    parameter = serializers.CharField(max_length=28)



