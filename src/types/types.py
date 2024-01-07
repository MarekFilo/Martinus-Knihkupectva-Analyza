from urllib.parse import urlparse


class Coordinates:
    def __init__(self, latitude: float, longitude: float):
        self.latitude = latitude
        self.longitude = longitude

    def __repr__(self):
        return f"Coordinates(latitude, longitude= {self.latitude}, {self.longitude})"

    def __getitem__(self, index):
        if index == 0:
            return self.latitude
        elif index == 1:
            return self.longitude
        else:
            raise IndexError(
                "Coordinates index out of range. Use 0 for latitude, 1 for longitude."
            )


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


class CSSSelector:
    def __init__(self, path: str):
        self.path = path

    def __repr__(self):
        return f"{self.path}"
