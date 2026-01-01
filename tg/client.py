# tg/client.py
import asyncio
from telegram import Bot
from telegram.error import TimedOut, NetworkError
from config import TELEGRAM_TOKEN, CHANNEL_ID, ADMIN_CHAT_ID

bot = Bot(token=TELEGRAM_TOKEN)

async def _send(chat_id, text, parse_mode=None):
    return await bot.send_message(
        chat_id=chat_id,
        text=text,
        parse_mode=parse_mode,
        disable_web_page_preview=True
    )

def send_channel_message(text, parse_mode=None, retries=3):
    async def runner():
        for i in range(retries):
            try:
                return await _send(CHANNEL_ID, text, parse_mode)
            except (TimedOut, NetworkError):
                if i == retries - 1:
                    raise
                await asyncio.sleep(2)

    return asyncio.run(runner())

def send_admin_message(text, parse_mode=None):
    async def runner():
        try:
            await _send(ADMIN_CHAT_ID, text, parse_mode)
        except Exception:
            pass  # heartbeat не должен падать

    asyncio.run(runner())

def pin_message(message_id):
    async def runner():
        try:
            await bot.pin_chat_message(
                chat_id=CHANNEL_ID,
                message_id=message_id,
                disable_notification=True
            )
        except Exception:
            pass

    asyncio.run(runner())

def unpin_all():
    async def runner():
        try:
            await bot.unpin_all_chat_messages(chat_id=CHANNEL_ID)
        except Exception:
            pass

    asyncio.run(runner())
