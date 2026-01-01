# formatter/status_formatter.py

def format_status(crypto_data, equity_data, snapshot):
    lines = []

    lines.append("━━━━━━━━━━━━")
    lines.append("MARKET STATUS")
    lines.append("━━━━━━━━━━━━")

    # --- CRYPTO ---
    if crypto_data and snapshot["crypto"]["regime"]:
        lines.append("")
        lines.append("CRYPTO")
        lines.append(f"Regime: {snapshot['crypto']['regime']}")
        lines.append(
            f"BTC: {crypto_data['btc_price']} "
            f"({crypto_data['btc_change_24h']}%)"
        )

    # --- EQUITY ---
    if equity_data and snapshot["equity"]["regime"]:
        lines.append("")
        lines.append("EQUITY")
        lines.append(f"Regime: {snapshot['equity']['regime']}")
        lines.append(
            f"SPX: {equity_data['spx_value']} "
            f"({equity_data['spx_change']}%)"
        )
        lines.append(
            f"DXY: {equity_data['dxy_value']} "
            f"({equity_data['dxy_change']}%)"
        )

    lines.append("")
    lines.append("━━━━━━━━━━━━")

    return "\n".join(lines)
