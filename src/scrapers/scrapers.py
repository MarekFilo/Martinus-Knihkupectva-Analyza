import requests
from bs4 import BeautifulSoup
from src.types.types import URL, XPath
from typing import List, Optional


class BasicScraper:
    def __init__(self, url: URL):
        self.url = url

    def scrape(self, xpath: XPath) -> Optional[List[str]]:
        try:
            response = requests.get(self.url)
            if response.status_code == 200:
                soup = BeautifulSoup(response.text, "html.parser")

                result = [element.get_text() for element in soup.select(xpath)]

                return result
            else:
                print(
                    f"Error: Unable to fetch URL\nStatus Code: {response.status_code}"
                )
                return None

        except Exception as e:
            print(f"Error: {e}")
            return None
