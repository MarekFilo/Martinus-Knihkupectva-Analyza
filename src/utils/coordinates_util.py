from src.types.types import Coordinates
from geopy.geocoders import Nominatim
from math import radians, sin, cos, sqrt, atan2
from typing import Optional
import re


def get_coordinates_for_city(city_name: str) -> Optional[Coordinates]:
    """
    Get geographic coordinates (latitude, longitude) for a given city.

    Parameters:
    - city_name (str): The name of the city.

    Returns:
    - Optional[Coordinates]: A tuple containing latitude and longitude, or None if coordinates are not found.
    """
    city_name = re.sub(
        r"\bUl\.\s*|\bul\.\s*|\bulica\b", "", city_name, flags=re.IGNORECASE
    )

    geolocator = Nominatim(user_agent="my_geocoder")
    if location := geolocator.geocode(city_name, country_codes="SK"):
        return Coordinates(latitude=location.latitude, longitude=location.longitude)

    print(f"Coordinates not found for {city_name}")
    return None


def haversine_distance(coord1: Coordinates, coord2: Coordinates) -> float:
    """
    Calculate the Haversine distance between two sets of geographic coordinates.

    Parameters:
    - coord1 (Coordinates): The first set of coordinates as a tuple (latitude, longitude).
    - coord2 (Coordinates): The second set of coordinates as a tuple (latitude, longitude).

    Returns:
    - float: The Haversine distance between the two coordinates in kilometers.
    """
    R = 6371.0

    lat1, lon1 = radians(coord1[0]), radians(coord1[1])
    lat2, lon2 = radians(coord2[0]), radians(coord2[1])

    dlat = lat2 - lat1
    dlon = lon2 - lon1

    # Haversine formula
    a = sin(dlat / 2) ** 2 + cos(lat1) * cos(lat2) * sin(dlon / 2) ** 2
    c = 2 * atan2(sqrt(a), sqrt(1 - a))

    return R * c
