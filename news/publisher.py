# news/publisher.py
from tg.client import send_channel_message

def publish_news(text):
    """
    Publish market news in monospace (terminal style)
    """
    message = f"<pre>{text}</pre>"
    send_channel_message(message, parse_mode="HTML")

def publish_status(text):
    """
    Publish market status in monospace (terminal style)
    """
    message = f"<pre>{text}</pre>"
    send_channel_message(message, parse_mode="HTML")
