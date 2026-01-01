# data/equity_data.py
import requests
import time

def fetch_equity_data():
    try:
        # S&P 500 (SPX)
        spx = requests.get(
            "https://stooq.com/q/d/l/",
            params={
                "s": "^spx",
                "i": "d"
            },
            timeout=10
        ).text.strip().splitlines()

        # Dollar Index (DXY)
        dxy = requests.get(
            "https://stooq.com/q/d/l/",
            params={
                "s": "dx.f",
                "i": "d"
            },
            timeout=10
        ).text.strip().splitlines()

        spx_today, spx_prev = spx[-1], spx[-2]
        dxy_today, dxy_prev = dxy[-1], dxy[-2]

        spx_close = float(spx_today.split(",")[4])
        spx_prev_close = float(spx_prev.split(",")[4])
        spx_change = ((spx_close - spx_prev_close) / spx_prev_close) * 100

        dxy_close = float(dxy_today.split(",")[4])
        dxy_prev_close = float(dxy_prev.split(",")[4])
        dxy_change = ((dxy_close - dxy_prev_close) / dxy_prev_close) * 100

        return {
            "spx_value": round(spx_close, 2),
            "spx_change": round(spx_change, 2),
            "dxy_value": round(dxy_close, 2),
            "dxy_change": round(dxy_change, 2),
            "timestamp": int(time.time())
        }

    except Exception as e:
        print(f"[EQUITY DATA ERROR] {e}")
        return None
