from dataclasses import dataclass
import requests
import logging
from unidecode import unidecode

logging.basicConfig(level=logging.INFO, filename="data.log", format="%(asctime)s %(levelname)s %(message)s")


@dataclass
class Article:
    title: str
    description: str


class News:
    def __init__(self, url, api_key):
        self.base_url = f"{url}&apikey={api_key}"

    def get_news(self):
        try:
            result = requests.get(self.base_url)
            result.raise_for_status()
            json_result = result.json()
            articles = json_result["articles"]
            return articles

        except requests.exceptions.RequestException as e:
            logging.error(f"Request Exception occurred: {e}")
            raise Exception("Something went wrong with the request")

    def return_news(self):
        try:
            all_articles = []
            for article in self.get_news():
                article_title = article["title"]
                article_description = article["description"]

                unicode_title = self.parse_text(article_title)
                unicode_description = self.parse_text(article_description)

                all_articles.append(Article(unicode_title, unicode_description))

            return all_articles

        except Exception as e:
            logging.error(f"Unhandled Exception occurred: {e}")
            raise Exception("An error occurred while processing the data")

    def parse_text(self, text: str) -> str | None:
        """ Removes Polish characters and leaves only those in the English alphabet """
        if text:
            return unidecode(text)
        else:
            return None

