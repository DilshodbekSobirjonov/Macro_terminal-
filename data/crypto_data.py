# data/crypto_data.py
import requests
import time

COINGECKO_URL = "https://api.coingecko.com/api/v3/simple/price"
GREED_URL = "https://api.alternative.me/fng/"

def fetch_crypto_greed():
    try:
        r = requests.get(GREED_URL, timeout=10).json()
        return int(r["data"][0]["value"])
    except Exception:
        return None

def fetch_crypto_data():
    try:
        r = requests.get(
            COINGECKO_URL,
            params={
                "ids": "bitcoin,ethereum",
                "vs_currencies": "usd",
                "include_24hr_change": "true"
            },
            timeout=10
        ).json()

        btc_price = round(r["bitcoin"]["usd"], 2)
        btc_change = round(r["bitcoin"]["usd_24h_change"], 2)
        eth_price = round(r["ethereum"]["usd"], 2)

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
