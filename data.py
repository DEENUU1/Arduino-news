from dataclasses import dataclass
import requests
import os
from dotenv import load_dotenv

load_dotenv()


@dataclass
class Article:
    title: str
    description: str


class News:
    def __init__(self, url, api_key):
        self.base_url = f"{url}&apikey={api_key}"

    def get_news(self):
        result = requests.get(self.base_url)
        json_result = result.json()
        articles = json_result["articles"]

        if result.status_code == 200:
            all_articles = []
            for article in articles:
                article_title = article["title"]
                article_description = article["description"]

                all_articles.append(Article(article_title, article_description))

            return all_articles
        else:
            raise Exception("Something went wrong with the request")


news = News("https://newsapi.org/v2/top-headlines?country=PL", os.getenv("NEWSAPI_KEY"))
print(news.get_news())