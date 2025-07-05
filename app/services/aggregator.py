from datetime import datetime
import random

def get_signal(symbol: str) -> dict:
    return {
        "symbol": symbol,
        "price": round(random.uniform(100.0, 200.0), 2),
        "volume": random.randint(1000, 10000),
        "timestamp": datetime.utcnow().isoformat()
    }