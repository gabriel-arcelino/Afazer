from flask import request, render_template, redirect, url_for, flash
from werkzeug.security import check_password_hash
from afazer.models import Atividade, Usuario, Pessoa
from flask_login import login_user, login_required, logout_user, current_user
from afazer.ext.grpc import conectar
# import grpc
# from afazer.ext.Usuario.usuarios_pb2_grpc import UsuariosStub
from afazer.ext.Usuario.usuarios_pb2 import Coluna, Requisicao


# canal = grpc.insecure_channel('localhost:50051')
cliente = conectar()


def login():
    if request.method == 'POST':

        email = request.form['email']
        senha = request.form.get('senha')
        remember = True if request.form.get('remember') else False
        usuario = Usuario.query.filter_by(login=email).first()
        # usuario = cliente.RetornarUsuarios(Requisicao(coluna=Coluna.LOGIN, valor=email))
        # resposta = Usuario.query.filter_by(login=email).first()

        if usuario is not None and check_password_hash(usuario.senha, senha):
            login_user(usuario, remember=remember)
            if current_user.tipo_usuario == "gestor":
                return redirect(url_for('webui.menu_gestorview'))
            return redirect(url_for('webui.menu_usuarioview'))
        flash("Email ou senha incorretos, tente novemente.")
        return render_template('loginUser.html')

    return render_template('loginUser.html')


@login_required
def sair():
    logout_user()
    return redirect(url_for('webui.login'))


@login_required
def visualizar_menu_gestor():
    if request.method == 'POST':
        pass
    atividades = Atividade.query.all()
    print(atividades)
    return render_template('atividades.html', atividades=atividades)


@login_required
def editar_atividade(id):
    if current_user.tipo_usuario =="gestor":
        if request.method == 'POST':
            nome = request.form.get('nome', type=str)
            responsavel = request.form.get('responsavel', type=str)
            atividade = Atividade.query.filter_by(id=id).first()
            atividade.nome = nome
            usuario = cliente.RetornarUsuarios(Requisicao(coluna=Coluna.NOME, valor=responsavel))
            atividade.responsavel = usuario.usuarios[0].nome
            atividade.save()
            return visualizar_menu_gestor()
        # usuarios = Usuario.query.filter_by(tipo_usuario="usuario")
        usuarios = [{'nome':"Pedro"}, {'nome':"Alexa"}]
        resposta = cliente.RetornarUsuarios(Requisicao(coluna=Coluna.TIPO_USUARIO, valor="usuario"))
        return render_template('editar_atividade_gestor.html', usuarios=resposta.usuarios)

    if request.method == 'POST':
        status = request.form.get('status', type=str)
        print(id, status)
        atividade = Atividade.query.filter_by(id=id).first()
        atividade.status = status
        atividade.save()
        flash("Atividade editada com sucesso.")
        return visualizar_menu_usuario()
    print("editar_atividade_usuario.html", id)
    return render_template('editar_atividade_usuario.html')


@login_required
def excluir_atividade(id):
    atividade=Atividade.query.filter_by(id=id).first()
    atividade.delete()
    return redirect(url_for('webui.menu_gestorview'))


@login_required
def criar_atividade():
    if request.method == 'POST':
        nome = request.form['nome']
        responsavel = request.form.get('responsavel')
        atividade=Atividade(nome=nome, responsavel=responsavel,status="Por Fazer")
        atividade.save()
        return redirect(url_for('webui.menu_gestorview'))
    resposta = cliente.RetornarUsuarios(Requisicao(coluna=Coluna.TIPO_USUARIO, valor="usuario"))
    return render_template('criar_atividade.html', usuarios=resposta.usuarios)


@login_required
def gerenciar_atividades():
    return render_template('gerenciar_atividades.html')


@login_required
def visualizar_menu_usuario():
    atividades = Atividade.query.filter_by(responsavel=current_user.pessoa.nome)
    return render_template('atividades.html', atividades=atividades)


