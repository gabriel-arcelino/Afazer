from afazer.Admin.ext import admin
from afazer.Admin.ext import db
from afazer.Admin.ext import auth
from flask import Flask
from afazer.Admin.models import Usuario, Pessoa
from concurrent import futures
from threading import Thread
from multiprocessing import Process
import grpc

from afazer.ext.Usuario.usuarios_pb2 import Coluna, Resposta, User
from afazer.ext.Usuario import usuarios_pb2_grpc


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
        if requisicao.coluna == Coluna.ID:
            print("if 1")
            usuario = Usuario.query.filter_by(id=requisicao.valor).first()
        elif requisicao.coluna == Coluna.NOME:
            pessoa = Pessoa.query.filter_by(nome=requisicao.valor).first()
            usuario = Usuario.query.filter_by(pessoa_id=pessoa.id)
        elif requisicao.coluna == Coluna.TIPO_USUARIO:
            usuario = Usuario.query.filter_by(tipo_usuario=requisicao.valor)

        else:
            context.abort(grpc.StatusCode.NOT_FOUND, "Requisicao nao encontrada")

        return Resposta(usuarios=copiarDados(usuario))


def copiarDados(usuarios):
    print("copiarDados")
    resposta=[]
    for usuario in usuarios:
        resposta.append(User(id=usuario.id, nome=usuario.pessoa.nome, login=usuario.login, senha=usuario.senha, tipo_usuario=usuario.tipo_usuario))
    return resposta


app = Flask(__name__)
app.config['TITLE'] = "Admin"
app.config["SECRET_KEY"]="c00ee353-52d1-4819-9b12-9cd86db93401"
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.iniciar_app(app)
admin.iniciar_app(app)
auth.init_app(app)




# @auth.verify_password
# def verificacao(login, senha):
#     if not (login, senha):
#         return False
#     return Usuarios.query.filter_by(login=login, senha=senha).first()


if __name__ == '__main__':
    # app.run(port=5001, debug=True)
    iniciarServidor()
    print("teste")
    # i = Process(target=iniciarServidor, args=None)
    # i.start()
    # i.join()
    #ssl_context='adhoc',