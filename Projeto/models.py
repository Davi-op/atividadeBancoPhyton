from Projeto import database , login_manager
from datetime import datetime
from flask_login import UserMixin

class Tarefas(database.Model, UserMixin):
    id = database.Column(database.Integer, primary_key=True)
    nomeTarefa = database.Column(database.String)
    id_admin = database.Column(database.Integer, database.ForeignKey('usuario.id'))
    id_usuario = database.Column(database.Integer, database.ForeignKey('usuario.id'))
    funcao = database.Column(database.String, nullable=False)

    @login_manager.user_loader
    def load_user(user_id):
        return Usuario.query.get(int(user_id))


class Usuario(database.Model):
        id = database.Column(database.Integer, primary_key=True)
        id_usuario = database.Column(database.Integer, database.ForeignKey('usuario.id'))
        id_admin = database.Column(database.Integer, database.ForeignKey('usuario.id'))
        username = database.Column(database.String, nullable=False)
        email = database.Column(database.String, nullable=False, unique=True)
        senha = database.Column(database.String, nullable=False)
        endereco = database.Column(database.String , nullable=False)
        telefone = database.Column(database.String, nullable=False)




