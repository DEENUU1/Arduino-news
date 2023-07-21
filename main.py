import serial
import time
from data import News
import os
from dotenv import load_dotenv

load_dotenv()

ser = serial.Serial("COM5", 9600, timeout=1)


def send_serial(data: str):
    """ Send serial data to arduino """
    try:
        ser.write(data.encode())

    except Exception as e:
        # logging.error(f"Error occurred while sending data to serial port: {e}")
        raise Exception("Failed to send data to Arduino")


def main():
    news = News("https://newsapi.org/v2/top-headlines?country=PL", os.getenv("NEWSAPI_KEY"))
    articles = news.return_news()
    
    for article in articles:
        data_to_send = f"{article.title} {article.description}"
        send_serial(data_to_send)

if __name__ == '__main__':
    main()
