# tg/client.py
import asyncio
from telegram import Bot
from telegram.error import TimedOut, NetworkError
from config import TELEGRAM_TOKEN, CHANNEL_ID, ADMIN_CHAT_ID

_bot = Bot(token=TELEGRAM_TOKEN)
_loop = asyncio.new_event_loop()
asyncio.set_event_loop(_loop)


async def _send(chat_id, text, parse_mode=None):
    return await _bot.send_message(
        chat_id=chat_id,
        text=text,
        parse_mode=parse_mode,
        disable_web_page_preview=True
    )


async def _pin(message_id):
    await _bot.pin_chat_message(
        chat_id=CHANNEL_ID,
        message_id=message_id,
        disable_notification=True
    )


async def _unpin_all():
    await _bot.unpin_all_chat_messages(chat_id=CHANNEL_ID)


def send_channel_message(text, parse_mode=None):
    try:
        return _loop.run_until_complete(
            _send(CHANNEL_ID, text, parse_mode)
        )
    except (TimedOut, NetworkError) as e:
        print(f"[TG SEND ERROR] {e}")
        return None


def send_admin_message(text, parse_mode=None):
    try:
        _loop.run_until_complete(
            _send(ADMIN_CHAT_ID, text, parse_mode)
        )
    except Exception:
        pass


def pin_message(message_id):
    try:
        _loop.run_until_complete(_pin(message_id))
    except Exception as e:
        print(f"[TG PIN ERROR] {e}")


def unpin_all():
    try:
        _loop.run_until_complete(_unpin_all())
    except Exception as e:
        print(f"[TG UNPIN ERROR] {e}")
