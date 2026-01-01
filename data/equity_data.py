# data/equity_data.py
import requests
import time

def _parse_stooq(symbol):
    r = requests.get(
        "https://stooq.com/q/d/l/",
        params={"s": symbol, "i": "d"},
        timeout=10
    )
    lines = r.text.strip().splitlines()

    # remove header
    if lines and lines[0].lower().startswith("date"):
        lines = lines[1:]

    if len(lines) < 2:
        return None

    def close_price(line):
        return float(line.split(",")[4])

    today = close_price(lines[-1])
    prev = close_price(lines[-2])
    change = ((today - prev) / prev) * 100

    return round(today, 2), round(change, 2)

def fetch_equity_data():
    try:
        spx = _parse_stooq("^spx")
        dxy = _parse_stooq("dx.f")

        if not spx or not dxy:
            return None

        spx_value, spx_change = spx
        dxy_value, dxy_change = dxy

        # --- Stock Greed proxy ---
        if spx_change < -0.5 and dxy_change > 0:
            greed_stock = 25   # fear
        elif spx_change > 0.5 and dxy_change < 0:
            greed_stock = 75   # greed
        else:
            greed_stock = 50   # neutral

        return {
            "spx_value": spx_value,
            "spx_change": spx_change,
            "dxy_value": dxy_value,
            "dxy_change": dxy_change,
            "greed_stock": greed_stock,
            "timestamp": int(time.time())
        }

    except Exception as e:
        print(f"[EQUITY DATA ERROR] {e}")
        return None
