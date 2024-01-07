from geopy.geocoders import Nominatim
from math import radians, sin, cos, sqrt, atan2


def get_coordinates_for_city(city_name):
    geolocator = Nominatim(user_agent="my_geocoder")
    location = geolocator.geocode(city_name)

    if location:
        return location.latitude, location.longitude
    else:
        print(f"Coordinates not found for {city_name}")
        return None


def haversine_distance(coord1, coord2):
    R = 6371.0

    lat1, lon1 = radians(coord1[0]), radians(coord1[1])
    lat2, lon2 = radians(coord2[0]), radians(coord2[1])

    dlat = lat2 - lat1
    dlon = lon2 - lon1

    # Haversine formula
    a = sin(dlat / 2) ** 2 + cos(lat1) * cos(lat2) * sin(dlon / 2) ** 2
    c = 2 * atan2(sqrt(a), sqrt(1 - a))

    distance = R * c

    return distance
