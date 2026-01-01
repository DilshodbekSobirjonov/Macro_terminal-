# logic/equity_regime.py

def detect_equity_regime(data):
    """
    Input:
      data = {
        spx_value: float,
        spx_change: float,   # % day change
        dxy_value: float,
        dxy_change: float,   # % day change
        timestamp: int
      }

    Output:
      {
        regime: str,
        bias: str,
        volatility: str
      }
    """

    spx_change = data["spx_change"]
    dxy_change = data["dxy_change"]

    # --- VOLATILITY (резкий стресс) ---
    if abs(spx_change) >= 2.0:
        return {
            "regime": "VOLATILITY",
            "bias": "BEARISH" if spx_change < 0 else "BULLISH",
            "volatility": "EXTREME"
        }

    # --- RISK-OFF ---
    # Акции падают, доллар растёт
    if spx_change < -0.7 and dxy_change > 0:
        return {
            "regime": "RISK-OFF",
            "bias": "BEARISH",
            "volatility": "ELEVATED"
        }

    # --- RISK-ON ---
    # Акции растут, доллар слабеет
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
        
