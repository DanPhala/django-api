# utils/fetch_lat_lng.py

from geopy.geocoders import Nominatim

def fetch_lat_lng(city_names):
    """
    Fetches latitude and longitude for the given city names.
    
    :param city_names: List of city names.
    :return: List of tuples containing city name and its latitude and longitude.
    """
    geolocator = Nominatim(user_agent="holiday_planner_api")
    results = []

    for city_name in city_names:
        location = geolocator.geocode(city_name.strip())
        if location:
            results.append((city_name.strip(), location.latitude, location.longitude))
        else:
            results.append((city_name.strip(), None, None))  # City not found

    return results
