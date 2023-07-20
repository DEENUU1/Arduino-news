from dataclasses import dataclass
import requests
import os
from dotenv import load_dotenv
import logging


load_dotenv()


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

            all_articles = []
            for article in articles:
                article_title = article["title"]
                article_description = article["description"]

                all_articles.append(Article(article_title, article_description))

            return all_articles
        except requests.exceptions.RequestException as e:
            logging.error(f"Request Exception occured: {e}")
            raise Exception("Something went wrong with the request")

        except Exception as e:
            logging.error(f"Unhandled Exception occured: {e}")
            raise Exception("An error occurred while processing the data")


news = News("https://newsapi.org/v2/top-headlines?country=PL", os.getenv("NEWSAPI_KEY"))
print(news.get_news())