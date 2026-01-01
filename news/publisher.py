from tg.client import send_message
from storage.state import can_publish_news, increment_news

def publish_news(text):
    if not can_publish_news():
        return
    send_message(text)
    increment_news()

