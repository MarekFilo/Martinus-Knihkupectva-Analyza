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
        self.url = url
        self.headers = {"User-Agent": user_agent}

    def _get_soup(self) -> Optional[BeautifulSoup]:
        try:
            response = requests.get(self.url, headers=self.headers)
            response.raise_for_status()
            return BeautifulSoup(response.text, "html.parser")
        except requests.RequestException as e:
            print(f"Error: {e}")
            return None

    def scrape(self, path: CSSSelector) -> Optional[List[str]]:
        if soup := self._get_soup():
            return [element.get_text() for element in soup.select(path)]
        return None
