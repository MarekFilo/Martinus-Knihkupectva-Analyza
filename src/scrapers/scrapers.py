import requests
from bs4 import BeautifulSoup
from src.types.types import URL, CSSSelector
from typing import List, Optional


class BasicScraper:
    def __init__(self, url: URL):
        self.url = url

    def _get_soup(self) -> Optional[BeautifulSoup]:
        try:
            response = requests.get(self.url)
            response.raise_for_status()
            soup = BeautifulSoup(response.text, "html.parser")
            return soup

        except requests.RequestException as e:
            print(f"Error: {e}")
            return None

    def scrape(self, path: CSSSelector) -> Optional[List[str]]:
        soup = self._get_soup()

        if soup:
            result = [element.get_text() for element in soup.select(path)]
            return result

        return None
