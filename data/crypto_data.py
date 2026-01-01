# data/crypto_data.py
import requests
import time

BINANCE_24H = "https://api.binance.com/api/v3/ticker/24hr"
GREED_URL = "https://api.alternative.me/fng/"

TIMEOUT = 10


def _get_symbol(symbol: str):
    """
    Fetch last price and 24h % change from Binance
    """
    r = requests.get(
        BINANCE_24H,
        params={"symbol": symbol},
        timeout=TIMEOUT
    )
    r.raise_for_status()
    j = r.json()

    price = float(j["lastPrice"])
    change = float(j["priceChangePercent"])

    return round(price, 2), round(change, 2)


def fetch_crypto_greed():
    """
    Crypto Fear & Greed Index (optional)
    If API is unreachable → return None
    """
    try:
        r = requests.get(GREED_URL, timeout=TIMEOUT)
        r.raise_for_status()
        j = r.json()
        return int(j["data"][0]["value"])
    except Exception:
        return None


def fetch_crypto_data():
    """
    Main crypto data fetcher
    Returns None if ANY critical data is missing
    """
    try:
        btc_price, btc_change = _get_symbol("BTCUSDT")
        eth_price, _ = _get_symbol("ETHUSDT")

        greed_crypto = fetch_crypto_greed()

        return {
            "btc_price": btc_price,
            "btc_change_24h": btc_change,
            "eth_price": eth_price,
            "greed_crypto": greed_crypto,
            "timestamp": int(time.time())
        }

    except Exception as e:
        print(f"[CRYPTO DATA ERROR] {e}")
        return None
