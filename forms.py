from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, TextField, TextAreaField, Form
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
   

# Review Form 
class ReviewForm(FlaskForm):
    movie_id = StringField('Movie ID', validators = [DataRequired(), Length(min=1, max=25)])
    movie_title = StringField('Movie Title', validators = [DataRequired(), Length(min=1, max=25)])
    poster_path = StringField('Poster Path', validators = [DataRequired(), Length(min=1, max=25)])
    movie_overview = StringField('Movie Overview', validators = [DataRequired(), Length(min=1, max=25)])
    search = TextField('', validators = [DataRequired(), Length(min=2, message=('Your message is too short.'))])
    review = TextAreaField('', validators = [DataRequired(), Length(min=1, max=400)])
    create = SubmitField(render_kw={"class": "btn-small submit-button"})