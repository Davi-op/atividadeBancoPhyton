from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired , Email , EqualTo , Length , ValidationError
from Projeto.models import Usuario

class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    senha = PasswordField('Senha', validators=[DataRequired(), Length(min=6)])
    botao_confirmacao = SubmitField('Fazer login')

class FormCriarConta(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    username = StringField('Usuario', validators=[DataRequired()])
    senha = PasswordField('Senha', validators=[DataRequired(), Length(min=6)])
    confirmacao_senha = PasswordField ('Confirmacao de Senha', validators=[DataRequired(), EqualTo('senha')])
    botao = (SubmitField('Cadastrar'))


    def validate_email(self, email):
        usuario = Usuario.query.filter_by(email=email.data).first()
        if usuario:
            raise ValidationError("Esse email ja esta cadastrado, crie outro ou faça login para continuar")