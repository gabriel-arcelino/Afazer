from sqlalchemy.ext.automap import automap_base
from sqlalchemy import create_engine, MetaData
from sqlalchemy.ext.declarative import declarative_base
from servidor_usuarios import config

Base = declarative_base()
engine = create_engine(f'postgresql+psycopg2://{config.user}:{config.password}@{config.host}:{config.port}/{config.database}')

metadata = MetaData(engine)
metadata.reflect()





