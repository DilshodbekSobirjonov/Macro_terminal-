# logic/equity_regime.py

def detect_equity_regime(data):
    """
    Input:
      data = {
        spx_value,
        spx_change,
        dxy_value,
        dxy_change,
        timestamp
      }

    Output:
      {
        regime,
        bias,
        volatility
      }
    """

    spx_change = data["spx_change"]
    dxy_change = data["dxy_change"]

    # --- RISK-OFF ---
    if spx_change < -1.0 and dxy_change > 0:
        return {
            "regime": "RISK-OFF",
            "bias": "BEARISH",
            "volatility": "ELEVATED"
        }

    # --- RISK-ON ---
    if spx_change > 0.5 and dxy_change < 0:
        return {
            "regime": "RISK-ON",
            "bias": "BULLISH",
            "volatility": "NORMAL"
        }

    # --- NEUTRAL ---
    return {
        "regime": "NEUTRAL",
        "bias": "NEUTRAL",
        "volatility": "NORMAL"
    }
