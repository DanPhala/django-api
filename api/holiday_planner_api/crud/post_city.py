from rest_framework.response import Response
from holiday_planner_api.serializers import WeatherRequestSerializer
from .get_city_weather import get_city_weather
from holiday_planner_api.utils.fetch_lat_lng import fetch_lat_lng

def post_city_weather(request):
    """Handle incoming weather request."""
    weather_serializer = WeatherRequestSerializer(data=request.data)

    if weather_serializer.is_valid():
        return process_weather_request(weather_serializer.validated_data)

    return Response(weather_serializer.errors, status=400)

def process_weather_request(validated_data):
    """Process weather request and return weather data for cities."""
    city_names = [name.strip() for name in validated_data['name'].split(',')]
    start_date = validated_data['start_date']
    end_date = validated_data['end_date']

    results = [get_city_weather(city_name, lat, lng, start_date, end_date) for city_name, lat, lng in fetch_lat_lng(city_names)]
    
    return Response(results, status=200)
