from geopy.geocoders import Nominatim


def get_coordinates_for_city(city_name):
    geolocator = Nominatim(user_agent="my_geocoder")
    location = geolocator.geocode(city_name)

    if location:
        return location.latitude, location.longitude
    else:
        print(f"Coordinates not found for {city_name}")
        return None
