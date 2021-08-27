from flask import Blueprint

from .views import login, visualizar_menu_gestor, gerenciar_atividades, visualizar_menu_usuario, sair, editar_atividade, criar_atividade, excluir_atividade

bp = Blueprint("webui", __name__, template_folder="templates")

login.methods = ['GET', 'POST']
visualizar_menu_usuario.methods=['GET','POST']
editar_atividade.methods = ['GET','POST']
criar_atividade.methods=['GET', 'POST']


bp.add_url_rule("/", view_func=login, endpoint="login")

bp.add_url_rule("/gestor", view_func=visualizar_menu_gestor, endpoint="menu_gestorview")
bp.add_url_rule("/gestor/criar_atvidade", view_func=criar_atividade,endpoint="criar_atividade_gestorview")
bp.add_url_rule("/editar_atividade/<int:id>", view_func=editar_atividade, endpoint="editar_atividade_gestorview")
bp.add_url_rule("/gestor/excluir_atividade/<int:id>", view_func=excluir_atividade,endpoint="excluir_atividade_gestorview")
bp.add_url_rule("/gestor/gerenciar_atividades", view_func=gerenciar_atividades, endpoint="gerenciaratividadesview")

bp.add_url_rule("/usuario/", view_func=visualizar_menu_usuario, endpoint="menu_usuarioview")
bp.add_url_rule("/usuario/editar_atividade/<int:id>", view_func=editar_atividade, endpoint="editar_atividade_usuarioview")


bp.add_url_rule("/usuario/sair/", view_func=sair, endpoint="sair")


# api.add_resource(Index, '/')
# api.add_resource(Pessoa, '/pessoa/<string:nome>/')
# api.add_resource(ListaPessoas, '/pessoa/')
# api.add_resource(ListaAtividades, '/atividades/')
# api.add_resource(Atividade, '/atividade/<int:id>/')


def iniciar_app(app):
    app.register_blueprint(bp)
