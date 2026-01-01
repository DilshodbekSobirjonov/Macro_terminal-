from datetime import date

_state = {"date": date.today(), "news": 0}

def reset():
    if _state["date"] != date.today():
        _state["date"] = date.today()
        _state["news"] = 0

def can_publish_news():
    reset()
    return _state["news"] < 10

def increment_news():
    _state["news"] += 1
