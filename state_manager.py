# state_manager.py
import time
import json
import os

STATE_FILE = "runtime_state.json"

# минимальное время подтверждения смены режима (сек)
CONFIRM_SECONDS = 60 * 30  # 30 минут

def _now():
    return int(time.time())

def _load_state():
    if not os.path.exists(STATE_FILE):
        return {
            "crypto": {"regime": None, "since": None},
            "equity": {"regime": None, "since": None},
            "last_publish": None
        }
    try:
        with open(STATE_FILE, "r") as f:
            return json.load(f)
    except Exception:
        return {
            "crypto": {"regime": None, "since": None},
            "equity": {"regime": None, "since": None},
            "last_publish": None
        }

def _save_state(state):
    with open(STATE_FILE, "w") as f:
        json.dump(state, f)

def _update_regime(prev, current):
    """
    Anti-flip:
    - если режим тот же → просто обновляем since (если пусто)
    - если режим изменился → ждём CONFIRM_SECONDS
    """
    if prev["regime"] == current["regime"]:
        if prev["since"] is None:
            prev["since"] = _now()
        return prev, False  # не изменился

    # режим новый
    if prev["since"] is None:
        return {"regime": current["regime"], "since": _now()}, False

    # проверка подтверждения
    if _now() - prev["since"] >= CONFIRM_SECONDS:
        return {"regime": current["regime"], "since": _now()}, True

    # ещё не подтверждён
    return prev, False

def process_state(crypto_regime, equity_regime):
    """
    Input:
      crypto_regime: dict or None
      equity_regime: dict or None

    Output:
      {
        publish: bool,
        snapshot: dict
      }
    """

    state = _load_state()
    changed = False

    # --- CRYPTO ---
    if crypto_regime is not None:
        new_crypto = {
            "regime": crypto_regime["regime"],
            "since": None
        }
        state["crypto"], ch = _update_regime(state["crypto"], new_crypto)
        changed = changed or ch

    # --- EQUITY ---
    if equity_regime is not None:
        new_equity = {
            "regime": equity_regime["regime"],
            "since": None
        }
        state["equity"], ch = _update_regime(state["equity"], new_equity)
        changed = changed or ch

    # решаем публиковать или нет
    publish = False
    if changed:
        # защита от спама
        if state["last_publish"] is None or _now() - state["last_publish"] >= CONFIRM_SECONDS:
            publish = True
            state["last_publish"] = _now()

    _save_state(state)

    return {
        "publish": publish,
        "snapshot": {
            "crypto": state["crypto"],
            "equity": state["equity"],
            "timestamp": _now()
        }
    }
