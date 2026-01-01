# data/equity_data.py
import yfinance as yf
import time

def fetch_equity_data():
    try:
        spx = yf.Ticker("^GSPC").history(period="2d")
        dxy = yf.Ticker("DX-Y.NYB").history(period="2d")

        spx_close = spx["Close"].iloc[-1]
        spx_prev = spx["Close"].iloc[-2]
        spx_change = ((spx_close - spx_prev) / spx_prev) * 100

        dxy_close = dxy["Close"].iloc[-1]
        dxy_prev = dxy["Close"].iloc[-2]
        dxy_change = ((dxy_close - dxy_prev) / dxy_prev) * 100

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
