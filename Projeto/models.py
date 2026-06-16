from Projeto import database, login_manager
from flask_login import UserMixin


@login_manager.user_loader
def load_user(user_id):
    return Usuario.query.get(int(user_id))

class Usuario(database.Model, UserMixin):
    __tablename__ = 'usuario'
    id = database.Column(
        database.Integer,
        primary_key=True
    )
    username = database.Column(
        database.String(50),
        nullable=False
    )
    email = database.Column(
        database.String(120),
        nullable=False,
        unique=True
    )
    senha = database.Column(
        database.String(255),
        nullable=False
    )
class Tarefas(database.Model):
    __tablename__ = 'tarefas'

    id = database.Column(
        database.Integer,
        primary_key=True
    )

    nomeTarefa = database.Column(
        database.String(100)
    )

    id_admin = database.Column(
        database.Integer,
        database.ForeignKey('usuario.id')
    )

    id_usuario = database.Column(
        database.Integer,
        database.ForeignKey('usuario.id')
    )

    funcao = database.Column(
        database.String(100),
        nullable=False
    )