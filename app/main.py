from fastapi import FastAPI
from app.models import SignalRequest
from app import services, storage

app = FastAPI(title="Financial Signal Aggregator")

@app.post("/aggregate")
async def aggregate_signals(req: SignalRequest):
    result = {}
    for symbol in req.symbols:
        price = await services.fetch_price_signal(symbol)
        storage.store_signal(f"{symbol}_price", price)
        entry = {"price": price}
        if req.include_volume:
            volume = await services.fetch_volume_signal(symbol)
            storage.store_signal(f"{symbol}_volume", volume)
            entry["volume"] = volume
        result[symbol] = entry
    return {"aggregated": result}

@app.get("/signals")
async def get_signals():
    return storage.get_all_signals()
