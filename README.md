# ===================== README.md =====================
# Financial Signal Aggregator

This project exposes a unified real-time financial signal interface via both REST (FastAPI) and gRPC. It simulates basic quote generation for testing quant system integration.

## Run REST server
```bash
uvicorn app.main:app --reload
```

## Run gRPC server
```bash
python app/grpc_server.py
```

## Generate gRPC code
```bash
python -m grpc_tools.protoc -I=app/protos --python_out=app/protos --grpc_python_out=app/protos app/protos/signal.proto
```
