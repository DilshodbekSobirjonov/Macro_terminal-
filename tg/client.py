from telegram import Bot
from config import TELEGRAM_TOKEN, CHANNEL_ID

bot = Bot(token=TELEGRAM_TOKEN)

def send_message(text):
    bot.send_message(chat_id=CHANNEL_ID, text=text)
