from typing import Dict

# 简单内存缓存
signal_store: Dict[str, float] = {}

def store_signal(key: str, value: float):
    signal_store[key] = value

def get_all_signals() -> Dict[str, float]:
    return signal_store
