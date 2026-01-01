# formatter/status_formatter.py
from datetime import datetime

def format_status(crypto, equity, snapshot):
    lines = []

    lines.append("<b>📌 MACRO TERMINAL — MARKET STATUS</b>")
    lines.append("")
    lines.append("━━━━━━━━━━━━━━━━━━")

    if crypto:
        lines.append("<b>CRYPTO</b>")
        lines.append(f"Regime: <b>{snapshot['crypto']['regime']}</b>")
        lines.append(f"BTC: <b>{crypto['btc_price']}</b> ({crypto['btc_change_24h']}%)")
        lines.append(f"ETH: <b>{crypto['eth_price']}</b>")
        if crypto.get("greed_crypto") is not None:
            lines.append(f"Fear & Greed (Crypto): <b>{crypto['greed_crypto']}</b>")
        lines.append("")
        lines.append("━━━━━━━━━━━━━━━━━━")

    if equity:
        lines.append("<b>EQUITY</b>")
        lines.append(f"Regime: <b>{snapshot['equity']['regime']}</b>")
        lines.append(f"SPX: <b>{equity['spx_value']}</b> ({equity['spx_change']}%)")
        lines.append(f"DXY: <b>{equity['dxy_value']}</b> ({equity['dxy_change']}%)")
        if equity.get("greed_stock") is not None:
            lines.append(f"Fear & Greed (Stock): <b>{equity['greed_stock']}</b>")
        lines.append("")
        lines.append("━━━━━━━━━━━━━━━━━━")

    lines.append(f"🕒 Updated: {datetime.utcnow().strftime('%H:%M UTC')}")

    return "\n".join(lines)
