import asyncio
from concurrent import futures

import grpc
from app.protos import signal_pb2_grpc, signal_pb2
from app.services.aggregator import get_signal

class SignalService(signal_pb2_grpc.SignalAggregatorServicer):
    async def GetSignal(self, request, context):
        symbol = request.symbol
        signal_value = get_signal(symbol)
        return signal_pb2.SignalReply(symbol=symbol, signal=signal_value)


async def serve():
    server = grpc.aio.server()
    signal_pb2_grpc.add_SignalAggregatorServicer_to_server(SignalService(), server)
    server.add_insecure_port('[::]:50051')
    await server.start()
    print("gRPC server listening on port 50051")
    await server.wait_for_termination()


if __name__ == "__main__":
    asyncio.run(serve())
