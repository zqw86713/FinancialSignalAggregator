


# Financial Signal Aggregator

A modular service for aggregating and serving real-time financial signals over both **gRPC** and **RESTful API** endpoints. Built for low-latency trading systems and quantitative research environments.

---

## 📦 Features

- ✅ **gRPC + FastAPI** dual-channel interface
- ⚙️ **Real-time signal simulation** from multiple market sources
- 🧩 **Extensible** architecture for signal routing, aggregation, and strategy integration
- 🚀 **Production-ready** layout with CI/testability in mind

---

## 🛠 Project Structure


```
FinancialSignalAggregator/
├── app/
│   ├── aggregator.py           # Core logic for signal computation
│   ├── grpc\_server.py          # gRPC server
│   ├── rest\_server.py          # FastAPI REST server
│   └── protos/
│       ├── signal.proto        # gRPC schema definition
│       ├── signal\_pb2.py       # Auto-generated gRPC messages
│       ├── signal\_pb2\_grpc.py  # Auto-generated gRPC service stubs
│       └── **init**.py
├── requirements.txt
└── README.md

```

---

## 🚀 Usage

### 1. Install dependencies

```bash
pip install -r requirements.txt
````

### 2. Compile gRPC files

```bash
python -m grpc_tools.protoc -I=app/protos --python_out=app/protos --grpc_python_out=app/protos app/protos/signal.proto
```

### 3. Start gRPC server

```bash
python -m app.grpc_server
```

### 4. Start REST API server

```bash
uvicorn app.rest_server:app --reload
```

---

## 📡 API Overview

### gRPC

* **Service:** `SignalService`
* **Method:** `GetSignal(SignalRequest) → SignalResponse`
* **Example Input:** `"symbol": "AAPL"`
* **Example Output:** `"price": 145.23`, `"timestamp": 1720452351`

### REST

* **GET** `/signal/{symbol}`
* **Response:**

```json
{
  "symbol": "AAPL",
  "price": 145.23,
  "timestamp": 1720452351
}
```

---

## 📈 Roadmap

* [ ] Add Redis/Kafka integration
* [ ] Add configurable signal computation logic
* [ ] Add unit & integration tests
* [ ] Add CI pipeline (GitHub Actions)
* [ ] Containerization (Docker)

---

## 👨‍💻 Author

**Qingwei Zhang** — Quant Developer Track
GitHub: [@zqw86713](https://github.com/zqw86713)
UChicago MADS | C++ | Python | Market Microstructure

---

## 📄 License

Apache 2.0 License (same as TensorFlow, QuickFIX, etc.)


