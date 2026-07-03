from flask import render_template, url_for, redirect
from flask_login import login_required, login_user, logout_user, current_user

from Projeto import app, database, bcrypt
from Projeto.forms import FormLogin, FormCriarConta, FormCriarTarefa
from Projeto.models import Usuario, Tarefa


@app.route('/', methods=['GET', 'POST'])
def homepage():
    formlogin = FormLogin()
    if formlogin.validate_on_submit():
        usuario = Usuario.query.filter_by(email=formlogin.email.data).first()
        if usuario and bcrypt.check_password_hash(usuario.senha, formlogin.senha.data):
            login_user(usuario)
            return redirect(url_for('perfil', id_usuario=usuario.id))
    return render_template('homepage.html', form=formlogin)


@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('homepage'))


@app.route('/criarconta', methods=['GET', 'POST'])
def criarconta():
    formcriarconta = FormCriarConta()

    if formcriarconta.validate_on_submit():
        senha = bcrypt.generate_password_hash(
            formcriarconta.senha.data
        ).decode('utf-8')

        usuario = Usuario(
            username=formcriarconta.username.data,
            email=formcriarconta.email.data,
            senha=senha,
            cargo=formcriarconta.cargo.data
        )

        database.session.add(usuario)
        database.session.commit()

        login_user(usuario)

        return redirect(url_for('perfil', id_usuario=usuario.id))

    return render_template(
        'criarconta.html',
        form=formcriarconta
    )


@app.route('/criartarefa', methods=['GET', 'POST'])
@login_required
def criartarefa():
    form = FormCriarTarefa()

    if form.validate_on_submit():

        funcionario = Usuario.query.get(form.id_responsavel.data)

        if funcionario:
            tarefa = Tarefa(
                titulo=form.titulo.data,
                descricao=form.descricao.data,
                id_responsavel=funcionario.id,
                id_criador=current_user.id,
                data_entrega=form.data_entrega.data,
                status=form.status.data,
                demanda=form.demanda.data
            )

            database.session.add(tarefa)
            database.session.commit()

            return redirect(url_for('perfil', id_usuario=current_user.id))

    return render_template(
        'criartarefa.html',
        form=form
    )


@app.route('/perfil/<id_usuario>')
@login_required
def perfil(id_usuario):
    if int(id_usuario) == (current_user.id):
        # o usuário está vendo o perfil dele
        return render_template("perfil.html", usuario=current_user)
    else:
        # Está vendo perfil de outra pessoa
        usuario = Usuario.query.get(int(id_usuario))
        return render_template('perfil.html', usuario=usuario)

@app.route('/feed')
@login_required
def feed():
        tarefas = Tarefa.query.order_by(Tarefa.data_criacao.desc() ).all()
        return render_template('feed.html', tarefas=tarefas )

