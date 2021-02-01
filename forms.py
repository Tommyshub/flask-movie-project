from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, TextField
from wtforms.validators import DataRequired, Email, EqualTo, Length

# Register form 
class RegistrationForm(FlaskForm):
    username = StringField('Username', validators = [DataRequired(), Length(min=4, max=25)])
    email = StringField('Email Address', validators = [DataRequired(), Length(min=4, max=25)])
    password = PasswordField('New Password', validators = [
        DataRequired(), EqualTo('confirm', message='Passwords must match')])
    confirm = PasswordField('Repeat Password')
    


# Login Form
class LoginForm(FlaskForm):
    username = StringField('Username', validators = [DataRequired(), Length(min=4, max=25)])
    password = PasswordField('Enter Password', validators = [DataRequired()])
    remember = BooleanField('Remember Me')
   
    


# Search Form
class SearchForm(FlaskForm):
    search = TextField('Search for Movie or Show', validators = [DataRequired(), 
    Length(min=4, message=('Your message is too short.'))])
    
    

# Save form 
class SaveForm(FlaskForm):
     submit = SubmitField('save')
   
    