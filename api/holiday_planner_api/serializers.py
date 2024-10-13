from rest_framework import serializers

class WeatherRequestSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=200)
    start_date = serializers.DateField()
    end_date = serializers.DateField()
