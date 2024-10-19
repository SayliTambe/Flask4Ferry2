from extensions import db
from wtforms.validators import DataRequired, Email, ValidationError
from wtforms import StringField, PasswordField, SubmitField
import bcrypt
import json
from flask_wtf import FlaskForm
from flask import current_app

class UserAuth(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)  

    password_hash = db.Column(db.String(128), nullable=False)

    def set_password(self, password):
        self.password_hash = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

    def check_password(self, password):
        return bcrypt.checkpw(password.encode('utf-8'), self.password_hash)


    def __repr__(self):
        return json.dumps({"name":self.name,"email":self.email})

    @property
    def db_uri(self):
        return current_app.config['SQLALCHEMY_DATABASE_URI_AUTH']




class RegisterForm(FlaskForm):
    name = StringField("Name", validators=[DataRequired()])
    email = StringField("Email", validators=[DataRequired(), Email()])
    password = PasswordField("Password",  
 validators=[DataRequired()])
    submit = SubmitField("Register")

    def validate_email(self, field):  

        user = UserAuth.query.filter_by(email=field.data).first()
        if user:
            raise ValidationError('Email Already Taken')

class LoginForm(FlaskForm):
    email = StringField("Email", validators=[DataRequired(), Email()])
    password = PasswordField("Password",  
 validators=[DataRequired()])  

    submit = SubmitField("Login")

