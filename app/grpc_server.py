import asyncio
from concurrent import futures
import grpc
from protos import signal_pb2_grpc, signal_pb2
from services.aggregator import get_signal

class SignalAggregator(signal_pb2_grpc.SignalAggregatorServicer):
    async def GetSignal(self, request, context):
        data = get_signal(request.symbol)
        return signal_pb2.SignalResponse(
            symbol=data["symbol"],
            price=data["price"],
            volume=data["volume"],
            timestamp=data["timestamp"]
        )

def serve():
    server = grpc.aio.server()
    signal_pb2_grpc.add_SignalAggregatorServicer_to_server(SignalAggregator(), server)
    server.add_insecure_port('[::]:50051')
    print("gRPC server listening on port 50051")
    asyncio.get_event_loop().run_until_complete(server.start())
    asyncio.get_event_loop().run_until_complete(server.wait_for_termination())

if __name__ == "__main__":
    serve()