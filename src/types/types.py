from urllib.parse import urlparse


class Coordinates:
    def __init__(self, latitude: float, longitude: float):
        """
        Represents geographic coordinates (latitude, longitude).

        Parameters:
        - latitude (float): The latitude value.
        - longitude (float): The longitude value.
        """
        self.latitude = latitude
        self.longitude = longitude

    def __repr__(self):
        """
        Return a string representation of the Coordinates object.

        Returns:
        - str: String representation in the format (latitude, longitude).
        """
        return f"({self.latitude}, {self.longitude})"

    def __getitem__(self, index):
        """
        Get the value at the specified index.

        Parameters:
        - index (int): The index to retrieve, 0 for latitude, 1 for longitude.

        Returns:
        - float: The latitude or longitude value.

        Raises:
        - IndexError: If the index is out of range.
        """
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
        """
        Represents a URL.

        Parameters:
        - url (str): The URL string.

        Raises:
        - ValueError: If the provided URL is invalid.
        """
        self.url = self.validate_url(url)

    def validate_url(self, url):
        """
        Validate the format of the provided URL.

        Parameters:
        - url (str): The URL to validate.

        Returns:
        - str: The validated URL.

        Raises:
        - ValueError: If the provided URL is invalid.
        """
        parsed_url = urlparse(url)
        if parsed_url.scheme and parsed_url.netloc:
            return url
        else:
            raise ValueError(f"Invalid URL: {url}")

    def __repr__(self):
        """
        Return a string representation of the URL object.

        Returns:
        - str: The URL string.
        """
        return self.url


class CSSSelector:
    def __init__(self, path: str):
        """
        Represents a CSS selector path.

        Parameters:
        - path (str): The CSS selector path.
        """
        self.path = path

    def __repr__(self):
        """
        Return a string representation of the CSSSelector object.

        Returns:
        - str: The CSS selector path.
        """
        return self.path
