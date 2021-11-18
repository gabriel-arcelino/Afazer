from flask import request, render_template, redirect, url_for, flash
from werkzeug.security import check_password_hash
from afazer.models import Pessoa, Atividade, Usuario
from flask_login import login_user, login_required, logout_user, current_user
import grpc
from afazer.ext.Usuario.usuarios_pb2_grpc import UsuariosStub
from afazer.ext.Usuario.usuarios_pb2 import Coluna, Requisicao

def conectarServidor(requisicao):
    canal = grpc.insecure_channel("localhost:50051")
    cliente = UsuariosStub(canal)
    return cliente.RetornarUsuarios()



def login():
    if request.method == 'POST':

        email = request.form['email']
        senha = request.form.get('senha')
        remember = True if request.form.get('remember') else False
        usuario = Usuario.query.filter_by(login=email).first()
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
            pessoa = Pessoa.query.filter_by(nome=responsavel).first()
            atividade.pessoa = pessoa
            atividade.save()
            return visualizar_menu_gestor()
        usuarios = Usuario.query.filter_by(tipo_usuario="usuario")
        return render_template('editar_atividade_gestor.html', usuarios=usuarios)

    if request.method == 'POST':
        status = request.form.get('status', type=str)
        print(id, status)
        atividade = Atividade.query.filter_by(id=id).first()
        atividade.status = status
        atividade.save()
        flash("Atividade editada com sucesso.")
        return visualizar_menu_usuario()
    print("'editar_atividade_usuario.html'", id)
    return render_template('editar_atividade_usuario.html')


def excluir_atividade(id):
    atividade=Atividade.query.filter_by(id=id).first()
    atividade.delete()
    return redirect(url_for('webui.menu_gestorview'))


def criar_atividade():
    if request.method == 'POST':
        nome = request.form['nome']
        responsavel = request.form.get('responsavel')
        pessoa=Pessoa.query.filter_by(nome=responsavel).first()
        atividade=Atividade(nome=nome,pessoa=pessoa,status="Por Fazer")
        atividade.save()
        return redirect(url_for('webui.menu_gestorview'))
    usuarios=Usuario.query.filter_by(tipo_usuario="usuario").all()
    return render_template('criar_atividade.html', usuarios=usuarios)


@login_required
def gerenciar_atividades():
    return render_template('gerenciar_atividades.html')


@login_required
def visualizar_menu_usuario():
    atividades = Atividade.query.filter_by(pessoa_id=current_user.pessoa_id)
    return render_template('atividades.html', atividades=atividades)

def post():
    dados = request.json
    try:
        pessoa = Pessoa.query.filter_by(nome=dados['pessoa']).first()
        atividade = Atividade(nome=dados['nome'], pessoa=pessoa)
        nomePessoa = atividade.pessoa.nome
        atividade.save()
        response = {
            'pessoa': nomePessoa,
            'nome': atividade.nome,
            'id': atividade.id
        }

    except AttributeError:
        response = {
            'status': 'error',
            'mensagem': 'Pessoa nao encontrada'
        }

    return response


# class Atividade():
    # def put(self, id):
    #     dados = request.json
    #     if not("Pendente" == dados['status'] or "Finalizado"):
    #         response = {
    #             'status': 'error',
    #             'mensagem': 'Dado recebido nao correponde ao esperado'
    #         }
    #         return response
    #
    #     atividade = Atividades.query.filter_by(id=id).first()
    #     atividade.status = dados['status']
    #     atividade.save()
    #     response = {
    #         'status': atividade.status
    #     }
    #     return response

    # def delete(self, id):
        # atividade = Atividades.query.filter_by(id=id).first()
        # #mensagem = 'Atividade {} excluida com sucesso'.format(atividade.nome)
        # mensagem = 'Atividade {} excluida com sucesso'
        # atividade.delete()
        # return {'status': 'sucesso', 'mensagem': mensagem}

