from Projeto import (
    app,
    bcrypt,
    database
)

from flask import (
    render_template,
    url_for,
    redirect
)

from flask_login import (
    login_user,
    login_required
)

from Projeto.forms import (
    LoginForm,
    FormCriarConta
)

from Projeto.models import Usuario

@app.route('/', methods=['GET', 'POST'])
def homepage():

    formLogin = LoginForm()

    return render_template(
        'homepage.html',
        form=formLogin
    )


@app.route('/criarconta', methods=['GET', 'POST'])
def criarconta():

    formcriarconta = FormCriarConta()

    if formcriarconta.validate_on_submit():

        try:

            senha = bcrypt.generate_password_hash(
                formcriarconta.senha.data
            ).decode('utf-8')

            usuario = Usuario(

                username=formcriarconta.username.data,

                email=formcriarconta.email.data,

                senha=senha
            )

            database.session.add(
                usuario
            )

            database.session.commit()

            login_user(
                usuario,
                remember=True
            )

            return redirect(
                url_for(
                    'perfil',
                    usuario=usuario.username
                )
            )

        except Exception as erro:

            database.session.rollback()

            print(erro)
    return render_template(
        'criarconta.html',
        form=formcriarconta
    )
@app.route('/perfil/<usuario>')
@login_required
def perfil(usuario):

    return render_template(
        'perfil.html',
        usuario=usuario
    )