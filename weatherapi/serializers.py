from rest_framework import serializers
from weatherapi.models import UserRequest
from weatherapi.models import WeatherData

class WeatherDataSerializer(serializers.ModelSerializer):

    class Meta:
        model = WeatherData
        fields = '__all__'

class UserRequestSerializer(serializers.ModelSerializer):
    weather_data = WeatherDataSerializer(many=True, read_only=True)
    class Meta:
        model = UserRequest
        fields = '__all__'