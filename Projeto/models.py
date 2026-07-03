from Projeto import database,login_manager
from datetime import datetime
from flask_login import UserMixin


class Usuario(database.Model, UserMixin):
    id = database.Column(database.Integer, primary_key=True)
    username = database.Column(database.String, nullable=False)
    email = database.Column(database.String, nullable=False, unique=True)
    senha = database.Column(database.String, nullable=False)
    cargo = database.Column(database.String, nullable=False)

    tarefas_recebidas = database.relationship(
        "Tarefa",
        foreign_keys="Tarefa.id_responsavel",
        backref="responsavel",
        lazy=True
    )

    tarefas_criadas = database.relationship(
        "Tarefa",
        foreign_keys="Tarefa.id_criador",
        backref="criador",
        lazy=True
    )

    @login_manager.user_loader
    def load_user(id_usuario):
        return Usuario.query.get(int(id_usuario))


class Tarefa(database.Model):
    id = database.Column(database.Integer, primary_key=True)

    id_responsavel = database.Column(database.Integer,database.ForeignKey('usuario.id'),nullable=False)

    id_criador = database.Column(database.Integer,database.ForeignKey('usuario.id'),nullable=False)

    data_criacao = database.Column(database.DateTime,nullable=False,default=datetime.utcnow)

    data_entrega = database.Column(database.DateTime,nullable=False)

    status = database.Column(database.String(20),nullable=False,default="Pendente"
    )

    demanda = database.Column(database.String,nullable=False,default='Normal')

    titulo = database.Column(database.String(100),nullable=False)

    descricao = database.Column(database.Text,nullable=False)