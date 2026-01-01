# tg/client.py
import asyncio
from telegram import Bot
from config import TELEGRAM_TOKEN, CHANNEL_ID, ADMIN_CHAT_ID

bot = Bot(token=TELEGRAM_TOKEN)

async def _send(chat_id, text, parse_mode=None):
    await bot.send_message(
        chat_id=chat_id,
        text=text,
        parse_mode=parse_mode,
        disable_web_page_preview=True
    )

async def _pin(message_id):
    await bot.pin_chat_message(
        chat_id=CHANNEL_ID,
        message_id=message_id,
        disable_notification=True
    )

async def _unpin_all():
    await bot.unpin_all_chat_messages(chat_id=CHANNEL_ID)

def send_channel_message(text, parse_mode=None):
    async def runner():
        msg = await bot.send_message(
            chat_id=CHANNEL_ID,
            text=text,
            parse_mode=parse_mode,
            disable_web_page_preview=True
        )
        return msg

    return asyncio.run(runner())

def send_admin_message(text, parse_mode=None):
    asyncio.run(_send(ADMIN_CHAT_ID, text, parse_mode))

def pin_message(message_id):
    asyncio.run(_pin(message_id))

def unpin_all():
    asyncio.run(_unpin_all())
