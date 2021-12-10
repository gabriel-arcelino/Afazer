import grpc, os
from Usuario.usuarios_pb2_grpc import UsuariosStub
# from afazer.ext.Usuario.usuarios_pb2 import Coluna, Requisicao


def conectar():
    with open(os.path.dirname(os.path.abspath(__file__))+'/server.crt', 'rb') as f:
        certificado = f.read()
    afazer_host = os.getenv("ADMIN_HOST", "localhost")
    credenciais_canal = grpc.ssl_channel_credentials(root_certificates=certificado)
    canal = grpc.secure_channel(f"{afazer_host}:50051", credenciais_canal)

    cliente = UsuariosStub(canal)
    return cliente