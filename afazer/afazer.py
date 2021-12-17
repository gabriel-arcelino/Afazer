from afazer.ext import admin
from afazer.ext import db
from afazer.ext import auth
from afazer.ext import aparencia
from flask import Flask
from afazer.blueprints import webui
from flask_login import LoginManager
from afazer.models import Usuario
from afazer.ext.grpc import conectar
from afazer.ext import autenticacao
from afazer import config

app = Flask(__name__)
app.config['TITLE'] = "Afazer"
app.secret_key = 'c59a5d3f-21e3-4dcc-b6f8-af91efd62463'
app.config['SQLALCHEMY_DATABASE_URI'] = config.DATABASE_CONNECTION_URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.app_context().push()

db.iniciar_app(app)
aparencia.iniciar_app(app)
#admin.iniciar_app(app)
#auth.init_app(app)
webui.iniciar_app(app)
autenticacao.iniciar_app(app)


if __name__ == '__main__':
    app.run(ssl_context='adhoc', host='0.0.0.0')
    # debug = True, host = '0.0.0.0', ssl_context = 'adhoc'
    #ssl_context='adhoc',