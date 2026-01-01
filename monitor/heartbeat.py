from tg.client import send_admin_message
from datetime import datetime, timezone

def heartbeat():
    now = datetime.now(timezone.utc).strftime("%H:%M UTC")
    send_admin_message(f"🟢 Macro Terminal alive · {now}")
