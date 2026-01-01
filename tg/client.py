# tg/client.py
from telegram import Bot
from config import TELEGRAM_TOKEN, CHANNEL_ID

bot = Bot(token=TELEGRAM_TOKEN)

def send_channel_message(text, parse_mode=None):
    bot.send_message(
        chat_id=CHANNEL_ID,
        text=text,
        parse_mode=parse_mode,
        disable_web_page_preview=True
    )
