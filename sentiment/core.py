from sentiment.ai_provider_1 import run_ai_1
from sentiment.ai_provider_2 import run_ai_2

def run_sentiment(facts):
    ai1 = run_ai_1(facts)
    ai2 = run_ai_2(facts)

    bullish = round((ai1["bullish"] + ai2["bullish"]) / 2)
    bearish = 100 - bullish

    bias = "Bullish" if bullish > bearish else "Bearish"

    return ai1, ai2, bullish, bearish, bias
