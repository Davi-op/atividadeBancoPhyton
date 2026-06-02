from Projeto import database
from datetime import datetime

class Tarefas(database.Model):
    id = database.Column(database.Integer, primary_key=True)
    nomeTarefa = database.Column(database.String)
    id_admin = database.Column(database.Integer, database.ForeignKey('usuario.id'))
    id_usuario = database.Column(database.Integer, database.ForeignKey('usuario.id'))
    funcao = database.Column(database.String, nullable=False)


class Usuario(database.Model):
        id = database.Column(database.Integer, primary_key=True)
        id_usuario = database.Column(database.Integer, database.ForeignKey('usuario.id'))
        id_admin = database.Column(database.Integer, database.ForeignKey('usuario.id'))
        username = database.Column(database.String, nullable=False)
        email = database.Column(database.String, nullable=False, unique=True)
        senha = database.Column(database.String, nullable=False)
        endereco = database.Column(database.String , nullable=False)
        telefone = database.Column(database.String, nullable=False)




