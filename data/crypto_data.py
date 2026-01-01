# data/crypto_data.py
import requests
import time

COINGECKO_URL = "https://api.coingecko.com/api/v3"

def fetch_crypto_data():
    try:
        btc = requests.get(
            f"{COINGECKO_URL}/simple/price",
            params={
                "ids": "bitcoin",
                "vs_currencies": "usd",
                "include_24hr_change": "true"
            },
            timeout=10
        ).json()

        global_data = requests.get(
            f"{COINGECKO_URL}/global",
            timeout=10
        ).json()

        return {
            "btc_price": btc["bitcoin"]["usd"],
            "btc_change_24h": btc["bitcoin"]["usd_24h_change"],
            "btc_dominance": global_data["data"]["market_cap_percentage"]["btc"],
            "timestamp": int(time.time())
        }

    except Exception as e:
        print(f"[CRYPTO DATA ERROR] {e}")
        return None
