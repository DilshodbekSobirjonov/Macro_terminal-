from telegram import Bot
from config import TELEGRAM_TOKEN, CHANNEL_ID

bot = Bot(token=8543769576:AAGmG7nQjuezf5OqHqzAWIZI1GJsP3b_Gyw)

def send_message(text):
    bot.send_message(chat_id=-1003534899420, text=text)
