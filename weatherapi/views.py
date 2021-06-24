from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from weatherapi.models import WeatherData, UserRequest
from weatherapi.serializers import WeatherDataSerializer, UserRequestSerializer
from weatherapi.city_ids import CITY_IDS
from time import strftime
import requests
import asyncio
import os

# Create your views here.
API_KEY = os.environ['API_KEY']

async def api_call(id):
    response = requests.get(
        f'http://api.openweathermap.org/data/2.5/weather?id={id}&appid={API_KEY}&units=metric'
    )
    return response


class UserRequestView(APIView):
    serializer_class = UserRequestSerializer

    def get(self, request, format=None):
        user_requests = UserRequest.objects.all()
        serializer = UserRequestSerializer(user_requests, many=True)
        print(request.headers)
        return Response(serializer.data)

    def post(self, request, format=None):
        user_id = request.query_params.get("id")

        user_request_data = {
            'user_id': user_id,
            'time': strftime("%Y-%m-%d %H:%M:%S")
        }
        user_request_serializer = UserRequestSerializer(data=user_request_data)
        if user_request_serializer.is_valid():
            user_request_serializer.save()

        print(user_request_serializer.data)
        
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        for id in CITY_IDS:
            response = loop.run_until_complete(api_call(id))
            weather_data = {
                'city_id': id,
                'temperature': response.json()['main']['temp'],
                'humidity': response.json()['main']['humidity'],
                'user_request': user_id
            }
            print(weather_data)

            weather_serializer = WeatherDataSerializer(data=weather_data, many=False)
            if weather_serializer.is_valid():
                weather_serializer.save()
        
        loop.close()

        return Response(user_request_serializer.data, status=status.HTTP_201_CREATED)


class WeatherDataView(APIView):
    serializer_class = WeatherDataSerializer
    
    def get(self, request, format=None):
        user_id = request.query_params.get("id")

        weather_data = WeatherData.objects.filter(user_request=user_id)
        percentage = round(len(weather_data) / len(CITY_IDS), 2)
        return Response(percentage)

