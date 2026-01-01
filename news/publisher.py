# news/publisher.py
from tg.client import send_channel_message, pin_message, unpin_all

def publish_news(text):
    message = f"<pre>{text}</pre>"
    send_channel_message(message, parse_mode="HTML")

def publish_status(text):
    message = f"<pre>{text}</pre>"

    # отправляем статус
    msg = send_channel_message(message, parse_mode="HTML")

    # снимаем старый pin и ставим новый
    try:
        unpin_all()
        pin_message(msg.message_id)
    except Exception as e:
        print(f"[PIN ERROR] {e}")
