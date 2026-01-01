# logic/crypto_regime.py

def detect_crypto_regime(data):
    """
    Input:
      data = {
        btc_price,
        btc_change_24h,
        btc_dominance,
        timestamp
      }

    Output:
      {
        regime,
        bias,
        volatility
      }
    """

    btc_change = data["btc_change_24h"]

    # --- VOLATILITY ---
    if abs(btc_change) >= 3.0:
        return {
            "regime": "VOLATILITY",
            "bias": "BEARISH" if btc_change < 0 else "BULLISH",
            "volatility": "EXTREME"
        }

    # --- RISK-OFF ---
    if btc_change < -1.0:
        return {
            "regime": "RISK-OFF",
            "bias": "BEARISH",
            "volatility": "ELEVATED"
        }

    # --- STABILIZATION ---
    if -1.0 <= btc_change <= 0.5:
        return {
            "regime": "STABILIZATION",
            "bias": "NEUTRAL",
            "volatility": "NORMALIZING"
        }

    # --- RISK-ON ---
    return {
        "regime": "RISK-ON",
        "bias": "BULLISH",
        "volatility": "NORMAL"
    }
