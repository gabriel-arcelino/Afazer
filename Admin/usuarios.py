from Admin.models import Usuario
from concurrent import futures
import grpc, os

from Usuario.usuarios_pb2 import Coluna, Resposta, User
from Usuario import usuarios_pb2_grpc


def iniciarServidor():
    print("Iniciar server")
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    usuarios_pb2_grpc.add_UsuariosServicer_to_server(
        UsuarioServe(), server
    )
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()


class UsuarioServe(usuarios_pb2_grpc.UsuariosServicer):
    def RetornarUsuarios(self, requisicao, context):
        usuario = ""
        if requisicao.coluna == Coluna.LOGIN:
            usuario = Usuario.query.filter_by(login=requisicao.valor)
            print("user",usuario)
        elif requisicao.coluna == Coluna.ID:
            usuario = Usuario.query.filter_by(id=requisicao.valor)
        elif requisicao.coluna == Coluna.NOME:
            usuario = Usuario.query.filter_by(nome=requisicao.valor)
        elif requisicao.coluna == Coluna.TIPO_USUARIO:
            usuario = Usuario.query.filter_by(tipo_usuario=requisicao.valor)
            print(usuario)

        else:
            context.abort(grpc.StatusCode.NOT_FOUND, "Requisicao nao encontrada")

        return Resposta(usuarios=copiarDados(usuario))


def copiarDados(usuarios):
    resposta=[]
    for usuario in usuarios:
        resposta.append(User(id=usuario.id, nome=usuario.nome, login=usuario.login, senha=usuario.senha, tipo_usuario=usuario.tipo_usuario))
    print(resposta)
    return resposta


if __name__ == '__main__':
    iniciarServidor()