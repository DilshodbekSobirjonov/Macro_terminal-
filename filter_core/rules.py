def market_event_pass(event, market):
    if event["type"] in ["RATE", "CPI", "NFP", "WAR", "SANCTIONS"]:
        return True

    if abs(market["BTC_change_pct"]) >= 3:
        return True

    if abs(market["SPX_change_pct"]) >= 1.5:
        return True

    return False
