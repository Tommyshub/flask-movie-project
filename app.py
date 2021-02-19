import os
import json
from flask import (
    Flask, flash, render_template,
    redirect, request, session, 
    url_for, abort, Blueprint, Response,)
from flask_pymongo import PyMongo

from bson.objectid import ObjectId
from error_handlers import error_handlers
from movie_search import movie_search
from auth import auth
from database import mongo
if os.path.exists("env.py"):
    import env

app = Flask(__name__)

# Blueprint for error handling
app.register_blueprint(error_handlers, url_prefix="/error/")
# Blueprint for movie routes 
app.register_blueprint(movie_search)
# Blueprint for authentication routes
app.register_blueprint(auth)
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
    return render_template("base.html")


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=False)