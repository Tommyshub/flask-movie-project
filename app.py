import os
from flask import (
    Flask, flash, render_template,
    redirect, request, session, url_for)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from forms import RegistrationForm, LoginForm

app = Flask(__name__)

app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")

mongo = PyMongo(app)


@app.route("/")
def index():
    return render_template("base.html")


# Render registration form 
@app.route("/register", methods=["POST", "GET"])
def register():
    form = RegistrationForm()
    return render_template("register.html", title="register", form=form)


# Render login form
@app.route("/login")
def login():
    form = LoginForm()
    return render_template("login.html", title="login", form=form)


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)