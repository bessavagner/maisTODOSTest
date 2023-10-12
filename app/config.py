import os


class Config:
    SECRET_KEY = 'chave_secreta_padrao'
    SQLALCHEMY_DATABASE_URI = 'postgresql://todos:maisTODOSLTDA@localhost:5437/todosLTDA'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

