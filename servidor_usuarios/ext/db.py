from flask_sqlalchemy import SQLAlchemy
from servidor_usuarios import config

engine = SQLAlchemy.create_engine(config.DATABASE_CONNECTION_URI)
