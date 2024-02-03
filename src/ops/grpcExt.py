
from grpc import StatusCode

# Exception Manager 
class ValArgumentError(Exception):
    def __init__(self, message, status_code=StatusCode.INVALID_ARGUMENT):
        self.status_code = status_code
        super().__init__(message)

# If your code connects to another gRPC server, you can write your logic here. For example:
"""
from grpc import insecure_channel
import protobuffers/external/mh_details_pb2_grpc as mh_details_pb2_gprc

class GRPCextension:

    def __init__(self):

        # Medical history details
        channel = insecure_channel(f'server_url_or_ip:port')
        self.mh_details_stub = mh_details_pb2_grpc.PatientStub(channel)


# Create an object to operate with other gRPC servers.
grpcExt = GRPCextension()

"""