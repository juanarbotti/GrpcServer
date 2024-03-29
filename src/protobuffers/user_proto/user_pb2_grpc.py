# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from protobuffers.user_proto import user_pb2 as protobuffers_dot_user__proto_dot_user__pb2


class UserStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.CreateUpdate = channel.unary_unary(
                '/user.User/CreateUpdate',
                request_serializer=protobuffers_dot_user__proto_dot_user__pb2.msg_user.SerializeToString,
                response_deserializer=protobuffers_dot_user__proto_dot_user__pb2.Id.FromString,
                )
        self.Get = channel.unary_unary(
                '/user.User/Get',
                request_serializer=protobuffers_dot_user__proto_dot_user__pb2.Id.SerializeToString,
                response_deserializer=protobuffers_dot_user__proto_dot_user__pb2.response_user.FromString,
                )
        self.Delete = channel.unary_unary(
                '/user.User/Delete',
                request_serializer=protobuffers_dot_user__proto_dot_user__pb2.Id.SerializeToString,
                response_deserializer=protobuffers_dot_user__proto_dot_user__pb2.Empty.FromString,
                )
        self.Search = channel.unary_unary(
                '/user.User/Search',
                request_serializer=protobuffers_dot_user__proto_dot_user__pb2.Element.SerializeToString,
                response_deserializer=protobuffers_dot_user__proto_dot_user__pb2.response_user_list.FromString,
                )


class UserServicer(object):
    """Missing associated documentation comment in .proto file."""

    def CreateUpdate(self, request, context):
        """Creates or modify users, whether or not 'id' is specified.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Get(self, request, context):
        """Get user
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Delete(self, request, context):
        """Delete user
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Search(self, request, context):
        """Search by username
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_UserServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'CreateUpdate': grpc.unary_unary_rpc_method_handler(
                    servicer.CreateUpdate,
                    request_deserializer=protobuffers_dot_user__proto_dot_user__pb2.msg_user.FromString,
                    response_serializer=protobuffers_dot_user__proto_dot_user__pb2.Id.SerializeToString,
            ),
            'Get': grpc.unary_unary_rpc_method_handler(
                    servicer.Get,
                    request_deserializer=protobuffers_dot_user__proto_dot_user__pb2.Id.FromString,
                    response_serializer=protobuffers_dot_user__proto_dot_user__pb2.response_user.SerializeToString,
            ),
            'Delete': grpc.unary_unary_rpc_method_handler(
                    servicer.Delete,
                    request_deserializer=protobuffers_dot_user__proto_dot_user__pb2.Id.FromString,
                    response_serializer=protobuffers_dot_user__proto_dot_user__pb2.Empty.SerializeToString,
            ),
            'Search': grpc.unary_unary_rpc_method_handler(
                    servicer.Search,
                    request_deserializer=protobuffers_dot_user__proto_dot_user__pb2.Element.FromString,
                    response_serializer=protobuffers_dot_user__proto_dot_user__pb2.response_user_list.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'user.User', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class User(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def CreateUpdate(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/user.User/CreateUpdate',
            protobuffers_dot_user__proto_dot_user__pb2.msg_user.SerializeToString,
            protobuffers_dot_user__proto_dot_user__pb2.Id.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Get(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/user.User/Get',
            protobuffers_dot_user__proto_dot_user__pb2.Id.SerializeToString,
            protobuffers_dot_user__proto_dot_user__pb2.response_user.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Delete(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/user.User/Delete',
            protobuffers_dot_user__proto_dot_user__pb2.Id.SerializeToString,
            protobuffers_dot_user__proto_dot_user__pb2.Empty.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Search(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/user.User/Search',
            protobuffers_dot_user__proto_dot_user__pb2.Element.SerializeToString,
            protobuffers_dot_user__proto_dot_user__pb2.response_user_list.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
