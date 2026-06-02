from Projeto import database, app
from Projeto.models import Tarefas , Usuario


with app.app_context():
    database.create_all()

