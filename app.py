
import os
import json
from flask import (
    Flask, flash, render_template,
    redirect, request, session, 
    url_for, abort, Blueprint, Response,)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash
from forms import RegistrationForm, LoginForm, SearchForm
from error_handlers import error_handlers
from movie_search import movie_search
from database import mongo
if os.path.exists("env.py"):
    import env

app = Flask(__name__)

# Blueprint for error_handlers.py
app.register_blueprint(error_handlers, url_prefix="/error/")
# Blueprint for the movie database 
app.register_blueprint(movie_search)
# Get database access from env.py
app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
# Get secret key from env.py
app.secret_key = os.environ.get("SECRET_KEY")
# Initiate PyMongo
mongo.init_app(app)



@app.route("/")
def base():
    """
    Route for the base template
    """
    return render_template("home.html")



@app.route("/register", methods=["POST", "GET"])
def register():
    """
    Route for user registration
    """
    # Registration form from forms.py
    form = RegistrationForm()
    if request.method == "POST":
        # check if username already exists in db
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})
        # Warn if the user already exists
        if existing_user:
            flash("Username already exists")
            return redirect(url_for("register"))
        # What to send to database 
        register = {
            "email": request.form.get("email").lower(),
            "username": request.form.get("username").lower(),
            "password": generate_password_hash(request.form.get("password"))
        }
        mongo.db.users.insert_one(register)

        # Put the new user into 'session' cookie
        session["user"] = request.form.get("username").lower()
        flash("Registration Successful!")
        return redirect(url_for("profile", username=session["user"]))
    
    return render_template("register.html", title="register", form=form)


# Route for user Login
@app.route("/login", methods=["POST", "GET"])
def login():
    """
    Route for user login
    """
    form = LoginForm()
    if request.method == "POST":
        # Check if the username exists in the database
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})
        # Check if the email exists in the database
        existing_email = mongo.db.users.find_one(
            {"email": request.form.get("email")})

        if existing_user:
            # Check if the hashed password match
            if check_password_hash(
                    existing_user["password"], request.form.get("password")):
                        session["user"] = request.form.get("username").lower()
                        flash("Welcome, {}".format(
                            request.form.get("username")))
                        return redirect(url_for(
                            "profile", username=session["user"]))
            
            else:
                # Invalid username or password
                flash("Incorrect Username and/or Password")
                return redirect(url_for("login"))

    return render_template("login.html", title="login", form=form)



@app.route("/profile/<username>", methods=["GET", "POST"])
def profile(username):
    """
    User Profile where the user can edit or delete the users own reviews.
    """
    if session.get('user'): # check if the user is logged in
        # Grab the session user's username from db
        username = mongo.db.users.find_one(
            {"username": session["user"]})["username"].capitalize()
        return render_template("profile.html", username=username, title="profile")
    return redirect(url_for("login"))



@app.route("/logout")
def logout():
    """
    User Logout by removing the user from the user session
    """
    # remove user from session cookie
    flash("You have been logged out")
    session.pop("user", None)
    return redirect(url_for("login"))


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)