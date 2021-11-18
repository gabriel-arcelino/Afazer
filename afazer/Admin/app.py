from afazer.ext import admin
from afazer.ext import db
from afazer.ext import auth
from flask import Flask
from afazer.models import Usuario
from concurrent import futures
import grpc

from afazer.ext.Usuario.usuarios_pb2 import Coluna, Resposta, User
from afazer.ext.Usuario import usuarios_pb2_grpc


def iniciarServidor():
    print("Iniciar server")
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    usuarios_pb2_grpc.add_UsuariosServicer_to_server(
        UsuarioServe(), server
    )
    server.add_insecure_port("[::]:50051")
    server.start()
    server.wait_for_termination()


class UsuarioServe(usuarios_pb2_grpc.UsuariosServicer):
    def RetornarUsuarios(self, requisicao, context):
        usuario = ""
        if requisicao.coluna == Coluna.ID:
            usuario = Usuario.query.filter_by(id=requisicao.valor).first()
        elif requisicao.coluna == Coluna.NOME:
            usuario = Usuario.query.filter_by(nome=requisicao.coluna).first()
        else:
            context.abort(grpc.StatusCode.NOT_FOUND, "Requisicao nao encontrada")

        return Resposta(copiarDados(usuario))


def copiarDados(usuario):
    return User(id=usuario.id, nome=usuario.nome, login=usuario.login, senha=usuario.senha, tipo_usuario=usuario.tipo_usuario)


app = Flask(__name__)
app.config['TITLE'] = "Admin"
db.iniciar_app(app)
admin.iniciar_app(app)
auth.init_app(app)




# @auth.verify_password
# def verificacao(login, senha):
#     if not (login, senha):
#         return False
#     return Usuarios.query.filter_by(login=login, senha=senha).first()


if __name__ == '__main__':
    app.run(port=5001, debug=True)
    iniciarServidor()
    #ssl_context='adhoc',