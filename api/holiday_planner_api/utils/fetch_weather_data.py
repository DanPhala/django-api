# utils/fetch_weather_data.py

import requests

def fetch_weather_data(latitude, longitude, start_date, end_date):
    """
    Fetches weather data for the given coordinates and date range.

    :param latitude: Latitude of the location.
    :param longitude: Longitude of the location.
    :param start_date: Start date for the weather forecast.
    :param end_date: End date for the weather forecast.
    :return: Weather data as a list of dictionaries.
    """
    base_url = "https://api.open-meteo.com/v1/forecast"
    params = {
        'latitude': latitude,
        'longitude': longitude,
        'start_date': start_date,
        'end_date': end_date,
        'daily': 'temperature_2m_max,temperature_2m_min',
        'timezone': 'auto'
    }
    response = requests.get(base_url, params=params)
    data = response.json()

    weather_data = []
    if 'daily' in data:
        for date, temp_max, temp_min in zip(
                data['daily']['time'],
                data['daily']['temperature_2m_max'],
                data['daily']['temperature_2m_min']):
            weather_data.append({
                'date': date,
                'max_temp': temp_max,
                'min_temp': temp_min
            })

    return weather_data
