import grpc,os
from Usuario.usuarios_pb2_grpc import UsuariosStub
# from afazer.ext.Usuario.usuarios_pb2 import Coluna, Requisicao


def conectar():
    afazer_host = os.getenv("AFAZER_HOST", "localhost")
    canal = grpc.insecure_channel(f"{afazer_host}:50051")
    cliente = UsuariosStub(canal)
    return cliente