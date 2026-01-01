from telegram.client import bot, CHANNEL_ID

def update_description(text):
    bot.set_chat_description(CHANNEL_ID, text)
