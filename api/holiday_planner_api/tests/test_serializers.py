import pytest
from holiday_planner_api.serializers import WeatherRequestSerializer

@pytest.mark.parametrize("data, is_valid", [
    ({"name": "New York", "start_date": "2024-10-01", "end_date": "2024-10-07"}, True),
])
def test_weather_request_serializer(data, is_valid):
    serializer = WeatherRequestSerializer(data=data)
    assert serializer.is_valid() == is_valid
