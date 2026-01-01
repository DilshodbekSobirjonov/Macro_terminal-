# main.py

from data.crypto_data import fetch_crypto_data
from data.equity_data import fetch_equity_data

from logic.crypto_regime import detect_crypto_regime
from logic.equity_regime import detect_equity_regime

from state_manager import process_state

from formatter.status_formatter import format_status
from news.publisher import publish_status


def run_cycle():
    crypto_data = fetch_crypto_data()
    equity_data = fetch_equity_data()

    crypto_regime = None
    equity_regime = None

    if crypto_data:
        crypto_regime = detect_crypto_regime(crypto_data)

    if equity_data:
        equity_regime = detect_equity_regime(equity_data)

    result = process_state(crypto_regime, equity_regime)

    if result["publish"]:
        text = format_status(
            crypto_data,
            equity_data,
            result["snapshot"]
        )
        publish_status(text)
