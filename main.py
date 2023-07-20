import serial
import time
from data import News
import os
from dotenv import load_dotenv

load_dotenv()


def send_serial(data, com):
    ser = serial.Serial(com, 9600, timeout=1)
    try:
        while True:
            ser.write(data.encode())
            time.sleep(1)
    except KeyboardInterrupt:
        ser.close()


def main():
    news_data = News("https://newsapi.org/v2/top-headlines?country=PL", os.getenv("NEWSAPI_KEY"))
    for data in news_data.get_news():
        if not data.description:
            str_data = data.title
            send_serial(str_data, "COM5")
        str_data = f"{data.title} {data.description}"
        send_serial(str_data, "COM5")


if __name__ == '__main__':
    main()
