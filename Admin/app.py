from Admin.ext import admin
from Admin.ext import db
from Admin.ext import auth
from flask import Flask
from Admin.models import Usuario
from concurrent import futures
import grpc

from Usuario.usuarios_pb2 import Coluna, Resposta, User
from Usuario import usuarios_pb2_grpc


app = Flask(__name__)
app.config['TITLE'] = "Admin"
app.config["SECRET_KEY"]="c00ee353-52d1-4819-9b12-9cd86db93401"
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///usuarios.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.iniciar_app(app)
admin.iniciar_app(app)
auth.init_app(app)





if __name__ == '__main__':
    app.run(port=5001, host='0.0.0.0', debug=True)
    print("teste")
    #ssl_context='adhoc',