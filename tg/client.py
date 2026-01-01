# tg/client.py
from telegram import Bot
from config import TELEGRAM_TOKEN, CHANNEL_ID, ADMIN_CHAT_ID

bot = Bot(token=TELEGRAM_TOKEN)

def send_channel_message(text, parse_mode=None):
    return bot.send_message(
        chat_id=CHANNEL_ID,
        text=text,
        parse_mode=parse_mode,
        disable_web_page_preview=True
    )

def send_admin_message(text, parse_mode=None):
    bot.send_message(
        chat_id=ADMIN_CHAT_ID,
        text=text,
        parse_mode=parse_mode,
        disable_web_page_preview=True
    )

def pin_message(message_id):
    bot.pin_chat_message(
        chat_id=CHANNEL_ID,
        message_id=message_id,
        disable_notification=True
    )

def unpin_all():
    bot.unpin_all_chat_messages(chat_id=CHANNEL_ID)
