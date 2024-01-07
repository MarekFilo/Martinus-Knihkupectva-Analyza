import requests
from bs4 import BeautifulSoup
from src.types.types import URL, CSSSelector
from typing import List, Optional


class BasicScraper:
    def __init__(
        self,
        url: URL,
        user_agent: str = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3",
    ):
        """
        Basic web scraper for extracting information from HTML content.

        Parameters:
        - url (URL): The URL to scrape.
        - user_agent (str): The user-agent string to use in the HTTP request headers.
        """
        self.url = url
        self.headers = {"User-Agent": user_agent}

    def _get_soup(self) -> Optional[BeautifulSoup]:
        """
        Retrieve the BeautifulSoup object from the HTML content of the specified URL.

        Returns:
        - Optional[BeautifulSoup]: The BeautifulSoup object representing the HTML content, or None if an error occurs.
        """
        try:
            response = requests.get(self.url, headers=self.headers)
            response.raise_for_status()
            return BeautifulSoup(response.text, "html.parser")
        except requests.RequestException as e:
            print(f"Error: {e}")
            return None

    def scrape(self, path: CSSSelector) -> Optional[List[str]]:
        """
        Scrape text content from the specified CSS selector path on the webpage.

        Parameters:
        - path (CSSSelector): The CSS selector path to locate the desired elements.

        Returns:
        - Optional[List[str]]: A list of text content from the selected elements, or None if an error occurs.
        """
        if soup := self._get_soup():
            return [element.get_text() for element in soup.select(path)]
        return None
