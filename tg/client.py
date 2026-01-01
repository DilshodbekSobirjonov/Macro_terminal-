from telegram import Bot
import os

TELEGRAM_TOKEN = os.getenv("TG_TOKEN")
CHANNEL_ID = os.getenv("TG_CHANNEL_ID")
ADMIN_CHAT_ID = os.getenv("ADMIN_CHAT_ID")

bot = Bot(token=TELEGRAM_TOKEN)

def send_channel_message(text):
    bot.send_message(chat_id=CHANNEL_ID, text=text)

def send_admin_message(text):
    bot.send_message(chat_id=ADMIN_CHAT_ID, text=text)
