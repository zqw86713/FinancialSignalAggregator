from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_aggregate_signals():
    response = client.post("/aggregate", json={"symbols": ["AAPL"], "include_volume": True})
    assert response.status_code == 200
    assert "AAPL" in response.json()["aggregated"]

def test_get_signals():
    response = client.get("/signals")
    assert response.status_code == 200
    assert isinstance(response.json(), dict)
