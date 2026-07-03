from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, SelectField, IntegerField, TextAreaField, DateField
from wtforms.validators import DataRequired,Email,EqualTo,Length,ValidationError


from Projeto.models import Usuario


class FormLogin(FlaskForm):
    email = StringField("Email", validators=[DataRequired(), Email()])
    senha = PasswordField("Senha", validators=[DataRequired(),])
    botao_confirmacao= SubmitField("Fazer Login")

class FormCriarConta(FlaskForm):
    email = StringField("Email", validators=[DataRequired(), Email()])
    username = StringField("Usuario", validators=[DataRequired()])
    senha =  PasswordField("Senha", validators=[DataRequired(),Length(min=6)])
    cargo = SelectField(
        "Cargo",
        choices=[
            ("usuario", "Usuário"),
            ("gerente", "Gerente")
        ]
    )
    confirmacao_senha = PasswordField("confirmacao a senha", validators=[DataRequired(),EqualTo("senha")])
    botao_confirmacao = SubmitField("Criar Conta")

    def validate_email(self, email):
        usuario = Usuario.query.filter_by(email=email.data).first()
        if usuario:
            raise ValidationError("Email ja cadastrado,faça login para continuar")

class FormCriarTarefa(FlaskForm):
    titulo = StringField('Título', validators=[DataRequired()])
    descricao = TextAreaField('Descrição', validators=[DataRequired()])
    id_responsavel = IntegerField(
        'Funcionário',
        validators=[DataRequired()]
    )

    data_entrega = DateField('Data de Entrega',format='%Y-%m-%d',validators=[DataRequired()])

    status = SelectField('Status',choices=[('Pendente', 'Pendente'),('Em andamento', 'Em andamento'),('Concluída', 'Concluída')],default='Pendente'
    )

    demanda = SelectField('Prioridade',choices=[('Baixa', 'Baixa'),('Normal', 'Normal'),('Alta', 'Alta'),('Urgente', 'Urgente')],default='Normal'
    )

    botao_criar = SubmitField('Criar Tarefa')