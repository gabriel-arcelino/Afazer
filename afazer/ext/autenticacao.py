from flask_login import LoginManager
from afazer.ext.grpc import conectar
from Usuario.usuarios_pb2 import Coluna, Requisicao
from afazer.models import Usuario
login_manager = LoginManager()


def iniciar_app(app):
    login_manager.login_view = 'webui.login'
    login_manager.init_app(app)

@login_manager.user_loader
def load_user(user_id):
    #since the user_id is just the primary key of our user table, use it in the query for the user
    print("Id: ", user_id)
    try:
        cliente = conectar()
        usuario=(cliente.RetornarUsuarios(Requisicao(coluna=Coluna.ID, valor=user_id))).usuarios[0]
        return Usuario(id=usuario.id, nome=usuario.nome, login=usuario.login, senha=usuario.senha, tipo_usuario=usuario.tipo_usuario)
    except IndexError:
        return None