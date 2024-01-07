from src.types.types import Coordinates
from geopy.geocoders import Nominatim
from math import radians, sin, cos, sqrt, atan2
from typing import Optional


def get_coordinates_for_city(city_name: str) -> Optional[Coordinates]:
    geolocator = Nominatim(user_agent="my_geocoder")
    if location := geolocator.geocode(city_name, country_codes="SK"):
        return Coordinates(latitude=location.latitude, longitude=location.longitude)

    print(f"Coordinates not found for {city_name}")
    return None


def haversine_distance(coord1: Coordinates, coord2: Coordinates) -> float:
    R = 6371.0

    lat1, lon1 = radians(coord1[0]), radians(coord1[1])
    lat2, lon2 = radians(coord2[0]), radians(coord2[1])

    dlat = lat2 - lat1
    dlon = lon2 - lon1

    # Haversine formula
    a = sin(dlat / 2) ** 2 + cos(lat1) * cos(lat2) * sin(dlon / 2) ** 2
    c = 2 * atan2(sqrt(a), sqrt(1 - a))

    return R * c
