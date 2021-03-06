import sys, os 
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import usuarios_pb2 as usuarios__pb2


class UsuariosStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.RetornarUsuarios = channel.unary_unary(
                '/Usuarios/RetornarUsuarios',
                request_serializer=usuarios__pb2.Requisicao.SerializeToString,
                response_deserializer=usuarios__pb2.Resposta.FromString,
                )


class UsuariosServicer(object):
    """Missing associated documentation comment in .proto file."""

    def RetornarUsuarios(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_UsuariosServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'RetornarUsuarios': grpc.unary_unary_rpc_method_handler(
                    servicer.RetornarUsuarios,
                    request_deserializer=usuarios__pb2.Requisicao.FromString,
                    response_serializer=usuarios__pb2.Resposta.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'Usuarios', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class Usuarios(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def RetornarUsuarios(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/Usuarios/RetornarUsuarios',
            usuarios__pb2.Requisicao.SerializeToString,
            usuarios__pb2.Resposta.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
