from collectors.market import fetch_market_data
from collectors.macro import fetch_macro_events
from filter_core.rules import market_event_pass
from formatter.news_formatter import format_news
from news.publisher import publish_news
from sentiment.core import run_sentiment
from tg.pin import update_pin

def scan_news():
    market = fetch_market_data()
    events = fetch_macro_events()

    for event in events:
        if market_event_pass(event, market):
            text = format_news(event, market)
            publish_news(text)

def daily_sentiment():
    market = fetch_market_data()
    facts = fetch_macro_events()

    ai1, ai2, bull, bear, bias = run_sentiment(facts)

    status = f"""
MACRO TERMINAL STATUS

Bias: {bias}

BTC {market['BTC_price']}
SPX {market['SPX_value']}
DXY {market['DXY']}
""".strip()

    update_pin(status)

def update_channel_description():
    pass

