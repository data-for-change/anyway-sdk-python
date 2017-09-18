import functools
import geocoder
import math
from collections import namedtuple

BoundingBox = namedtuple("BoundingBox", ["lat_min", "lon_min", "lat_max", "lon_max"])

_EARTH_RADIUS_IN_KM = 6371

def get_bounding_box(*, latitude, longitude, distance_in_km):
    assert distance_in_km > 0
    assert latitude >= -90.0 and latitude <= 90.0
    assert longitude >= -180.0 and longitude <= 180.0

    lat = math.radians(latitude)
    lon = math.radians(longitude)

    parallel_radius = _EARTH_RADIUS_IN_KM * math.cos(lat)

    lat_min = lat - distance_in_km / _EARTH_RADIUS_IN_KM
    lat_max = lat + distance_in_km / _EARTH_RADIUS_IN_KM
    lon_min = lon - distance_in_km / parallel_radius
    lon_max = lon + distance_in_km / parallel_radius


    return BoundingBox(
        lat_min=math.degrees(lat_min),
        lon_min=math.degrees(lon_min),
        lat_max=math.degrees(lat_max),
        lon_max=math.degrees(lon_max))


@functools.lru_cache(maxsize=32)
def _get_coordinates(location):
    coordinates = geocoder.google(location)
    return coordinates.lat, coordinates.lng


def get_location_bounding_box(*, location, distance_in_km):
    lat, lng = _get_coordinates(location)
    return get_bounding_box(latitude=lat, longitude=lng, distance_in_km=distance_in_km)
