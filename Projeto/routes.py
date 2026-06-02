from Projeto import app
from flask import render_template

@app.route('/')
def homepage():
    return render_template('homepage.html')

@app.route('/perfil/<usuario>')
def perfil(usuario):
    return render_template('perfil.html', usuario=usuario)