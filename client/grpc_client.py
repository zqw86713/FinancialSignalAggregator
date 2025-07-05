import grpc
from app.protos import signal_pb2, signal_pb2_grpc

def run():

    channel = grpc.insecure_channel('localhost:50051')
    stub = signal_pb2_grpc.SignalAggregatorStub(channel)


    request = signal_pb2.SignalRequest(symbol='AAPL')


    try:
        response = stub.GetSignal(request)
        print(f"Received signal: {response.signal} for symbol {request.symbol}")
    except grpc.RpcError as e:
        print(f"RPC failed: {e.code()} - {e.details()}")

if __name__ == '__main__':
    run()
