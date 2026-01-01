from telegram import Bot
from config import TELEGRAM_TOKEN, CHANNEL_ID

bot = Bot(token=TELEGRAM_TOKEN)

def send_channel_message(text):
    bot.send_message(chat_id=CHANNEL_ID, text=text)

def send_admin_message(text):
    bot.send_message(chat_id=ADMIN_CHAT_ID, text=text)
