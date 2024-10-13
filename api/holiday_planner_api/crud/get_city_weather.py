from holiday_planner_api.utils.fetch_weather_data import fetch_weather_data

def get_city_weather(city_name, latitude, longitude, start_date, end_date):
    """Fetch weather data for a given city."""
    if latitude is not None and longitude is not None:
        weather_data = fetch_weather_data(latitude, longitude, start_date, end_date)
        return {
            'city': city_name,
            'start_date': start_date,
            'end_date': end_date,
            'weather_data': weather_data
        }
    return {
        'city': city_name,
        'error': 'City not found'
    }
