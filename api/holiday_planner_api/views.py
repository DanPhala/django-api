from rest_framework import generics
from rest_framework.response import Response
from .serializers import WeatherRequestSerializer
from .crud.delete_all import delete_all_destinations
from .crud.post_city import post_city_weather
from .models import Destination

class DestinationListCreate(generics.ListCreateAPIView):
    queryset = Destination.objects.all()  # pylint: disable=no-member
    serializer_class = WeatherRequestSerializer

    def delete(self, request, *args, **kwargs):
        """Delete all destination records."""
        return delete_all_destinations(request)

    def post(self, request, *args, **kwargs):
        """Handle incoming weather requests."""
        return post_city_weather(request)
