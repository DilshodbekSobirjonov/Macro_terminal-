from telegram import Bot
import os
import asyncio

TELEGRAM_TOKEN = os.getenv("TG_TOKEN")
CHANNEL_ID = os.getenv("TG_CHANNEL_ID")
ADMIN_CHAT_ID = os.getenv("ADMIN_CHAT_ID")

bot = Bot(token=TELEGRAM_TOKEN)

async def _send(chat_id, text):
    await bot.send_message(chat_id=chat_id, text=text)

def send_channel_message(text):
    asyncio.run(_send(CHANNEL_ID, text))

def send_admin_message(text):
    asyncio.run(_send(ADMIN_CHAT_ID, text))
