from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from afazer.ext.db import db
from flask_login import UserMixin


class Atividade(db.Model):
    __tablename__ = 'atividade'
    id = Column(Integer, primary_key=True)
    nome = Column(String(80), index=True)
    responsavel = Column(String(80))
    status = Column(String(80))

    def __repr__(self):
        return '<Atividades {}>'.format(self.nome)

    def save(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()


class Usuario(db.Model, UserMixin):
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



