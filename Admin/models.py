from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from Admin.ext.db import db, Base
from flask_login import UserMixin


class Usuario(Base, UserMixin):
    __tablename__ = 'usuario'
    id = Column(Integer, primary_key=True)
    nome = Column(String(60))
    login = Column(String(20), unique=True)
    senha = Column(String(20))
    tipo_usuario = Column(String(20))

    def __repr__(self):
        return '<Usuario {}>'.format(self.login)

    def save(self):
        db.add(self)
        db.commit()

    def delete(self):
        db.delete(self)
        db.commit()



