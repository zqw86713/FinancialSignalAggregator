import asyncio
import random

async def fetch_price_signal(symbol: str) -> float:
    await asyncio.sleep(0.05)
    return round(random.uniform(100, 200), 2)

async def fetch_volume_signal(symbol: str) -> float:
    await asyncio.sleep(0.05)
    return round(random.uniform(1000, 5000), 0)
