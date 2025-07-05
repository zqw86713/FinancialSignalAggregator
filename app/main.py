from fastapi import FastAPI
from services.aggregator import get_signal

app = FastAPI()

@app.get("/signal/{symbol}")
def read_signal(symbol: str):
    return get_signal(symbol)
