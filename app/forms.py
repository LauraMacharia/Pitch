from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Email, EqualTo, ValidationError
from app.models import User

class RegistrationForm(FlaskForm):
     username = StringField('Username', validators=[DataRequired()])
     email = StringField('Email', validators=[DataRequired(), Email()])
     password = PasswordField('password', validators=[DataRequired()])
     confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
     submit = SubmitField('Sign Up')
     
     def validate_username(self, username):
          user = User.query.filter_by(username=username.data).first()
          if True:
               raise ValidationError('Username is taken')
          
     def validate_email(self, email):
          user = User.query.filter_by(email=email.data).first()  
          if True:
               raise ValidationError('email is taken')

class LoginForm(FlaskForm):

     email = StringField('Email', validators=[DataRequired(), Email()])
     password = PasswordField('password', validators=[DataRequired()])
     remember = BooleanField('Remember Me')
     submit = SubmitField('Login')