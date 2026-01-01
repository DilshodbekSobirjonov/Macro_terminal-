import os
from dotenv import load_dotenv

load_dotenv()

TELEGRAM_TOKEN = os.getenv("TG_TOKEN")
CHANNEL_ID = os.getenv("TG_CHANNEL_ID")
ADMIN_CHAT_ID = os.getenv("ADMIN_CHAT_ID")

AI_PROVIDER_1_KEY = os.getenv("AI1_KEY")
AI_PROVIDER_2_KEY = os.getenv("AI2_KEY")

TIMEZONE = "UTC"
