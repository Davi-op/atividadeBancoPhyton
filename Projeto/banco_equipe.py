from Projeto import database, app
from Projeto.models import Usuario, Foto

with app.app_context():
    database.create_all()