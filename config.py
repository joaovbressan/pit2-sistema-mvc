import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'chave-secreta-pit2-bressan'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///estoque_vendas.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
