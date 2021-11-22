import grpc
from afazer.ext.Usuario.usuarios_pb2_grpc import UsuariosStub
from afazer.ext.Usuario.usuarios_pb2 import Coluna, Requisicao


def conectar():
    canal = grpc.insecure_channel('localhost:50051')
    cliente = UsuariosStub(canal)
    return cliente