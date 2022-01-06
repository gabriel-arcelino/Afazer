from sqlalchemy import Table, Column, String, Integer
from servidor_usuarios.ext.db import metadata, Base, engine
from sqlalchemy.orm import sessionmaker, Session


class Usuario(Base):
    __tablename__ = Table("usuario", metadata)
    id = Column(Integer, primary_key=True)
    nome = Column(String(60))
    login = Column(String(30), unique=True)
    senha = Column(String(150))
    tipo_usuario = Column(String(20))


Session = sessionmaker(engine)
sessao = Session()




