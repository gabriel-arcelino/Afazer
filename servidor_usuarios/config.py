import os
# os.environ['POSTGRES_USER']='gabriel'
# os.environ['POSTGRES_PASSWORD']='senha1'
# os.environ['POSTGRES_HOST']='localhost'
# os.environ['POSTGRES_PORT']='5432'
# os.environ['POSTGRES_DB']='usuarios'


user = os.environ['POSTGRES_USER']
password = os.environ['POSTGRES_PASSWORD']
host = os.environ['POSTGRES_HOST']
database = os.environ['POSTGRES_DB']
port = os.environ['POSTGRES_PORT']


DATABASE_CONNECTION_URI = f'postgresql+psycopg2://{user}:{password}@{host}:{port}/{database}'
