# monitor/heartbeat.py
import time
from tg.client import send_admin_message

def heartbeat():
    ts = time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime())
    send_admin_message(
        f"<pre>Men tirikman xo'jayin 🫡\nUTC {ts}</pre>",
        parse_mode="HTML"
    )
