def format_news(event, market):
    return f"""
━━━━━━━━━━━━
MARKET NEWS
━━━━━━━━━━━━

• Event: {event['description']}
• Reaction: {event['reaction']}
• BTC: {market['BTC_change_pct']}%

━━━━━━━━━━━━
Greed Crypto {market['greed_crypto']} | Greed Stock {market['greed_stock']}
Altseason {market['altseason']}
""".strip()
