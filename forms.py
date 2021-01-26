from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, TextField
from wtforms.validators import DataRequired, Email, EqualTo, Length
import os
if os.path.exists("env.py"):
    import env

secret_key = os.environ.get("SECRET_KEY")

# Register form 
class RegistrationForm(FlaskForm):
    username = StringField('Username', validators = [DataRequired(), Length(min=4, max=25)])
    email = StringField('Email Address', validators = [DataRequired(), Length(min=4, max=25)])
    password = PasswordField('New Password', validators = [
        DataRequired(), EqualTo('confirm', message='Passwords must match')])
    confirm = PasswordField('Repeat Password')
    submit = SubmitField()


# Login Form
class LoginForm(FlaskForm):
    username = StringField('Username', validators = [DataRequired(), Length(min=4, max=25)])
    password = PasswordField('Enter Password', validators = [DataRequired()])
    remember = BooleanField('Remember Me')
    submit = SubmitField()


# Search Form
class SearchForm(FlaskForm):
    search = TextField('Search for Movie or Show', validators = [DataRequired(), 
    Length(min=4, message=('Your message is too short.'))])
    submit = SubmitField('Submit')