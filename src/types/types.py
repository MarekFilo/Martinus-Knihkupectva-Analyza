from typing import Tuple
from urllib.parse import urlparse
from typing import List


class Coordinates:
    def __init__(self, latitude: float, longitude: float):
        self.latitude = latitude
        self.longitude = longitude

    def __repr__(self):
        return f"Coordinates(latitude={self.latitude}, longitude={self.longitude})"


class URL:
    def __init__(self, url: str):
        self.url = self.validate_url(url)

    def validate_url(self, url):
        parsed_url = urlparse(url)
        if parsed_url.scheme and parsed_url.netloc:
            return url
        else:
            raise ValueError(f"Invalid URL: {url}")

    def __repr__(self):
        return f"URL(url={self.url})"


class XPath:
    def __init__(self, path: str):
        self.path = path

    def __repr__(self):
        return f"XPath(path={self.path})"