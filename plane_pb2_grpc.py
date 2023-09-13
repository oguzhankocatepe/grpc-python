# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import plane_pb2 as plane__pb2


class PlaneServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.CreatePlane = channel.unary_unary(
                '/PlaneService/CreatePlane',
                request_serializer=plane__pb2.PlaneNoId.SerializeToString,
                response_deserializer=plane__pb2.Plane.FromString,
                )
        self.GetPlanes = channel.unary_unary(
                '/PlaneService/GetPlanes',
                request_serializer=plane__pb2.GetPlanesRequest.SerializeToString,
                response_deserializer=plane__pb2.Planes.FromString,
                )
        self.StreamPlanes = channel.unary_stream(
                '/PlaneService/StreamPlanes',
                request_serializer=plane__pb2.GetPlanesStreamRequest.SerializeToString,
                response_deserializer=plane__pb2.Planes.FromString,
                )


class PlaneServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def CreatePlane(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetPlanes(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def StreamPlanes(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_PlaneServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'CreatePlane': grpc.unary_unary_rpc_method_handler(
                    servicer.CreatePlane,
                    request_deserializer=plane__pb2.PlaneNoId.FromString,
                    response_serializer=plane__pb2.Plane.SerializeToString,
            ),
            'GetPlanes': grpc.unary_unary_rpc_method_handler(
                    servicer.GetPlanes,
                    request_deserializer=plane__pb2.GetPlanesRequest.FromString,
                    response_serializer=plane__pb2.Planes.SerializeToString,
            ),
            'StreamPlanes': grpc.unary_stream_rpc_method_handler(
                    servicer.StreamPlanes,
                    request_deserializer=plane__pb2.GetPlanesStreamRequest.FromString,
                    response_serializer=plane__pb2.Planes.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'PlaneService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class PlaneService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def CreatePlane(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/PlaneService/CreatePlane',
            plane__pb2.PlaneNoId.SerializeToString,
            plane__pb2.Plane.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetPlanes(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/PlaneService/GetPlanes',
            plane__pb2.GetPlanesRequest.SerializeToString,
            plane__pb2.Planes.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def StreamPlanes(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(request, target, '/PlaneService/StreamPlanes',
            plane__pb2.GetPlanesStreamRequest.SerializeToString,
            plane__pb2.Planes.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)