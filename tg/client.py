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

def _run(coro):
    try:
        loop = asyncio.get_running_loop()
    except RuntimeError:
        loop = None

    if loop and loop.is_running():
        asyncio.create_task(coro)
    else:
        asyncio.run(coro)

def send_channel_message(text, parse_mode=None):
    _run(_send(CHANNEL_ID, text, parse_mode))

def send_admin_message(text, parse_mode=None):
    _run(_send(ADMIN_CHAT_ID, text, parse_mode))
