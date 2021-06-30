import os
import json
import redis
from flask import (
    Flask, flash, render_template,
    redirect, request, session,
    url_for, abort, Blueprint, Response,)
from flask_pymongo import PyMongo

from bson.objectid import ObjectId
from error_handlers import error_handlers
from movies import movies
from auth import auth
from database import mongo
from flask_session import Session


if os.path.exists("env.py"):
    import env

app = Flask(__name__)

# Blueprint for error handling
app.register_blueprint(error_handlers, url_prefix="/error/")
# Blueprint for movie routes
app.register_blueprint(movies)
# Blueprint for authentication routes
app.register_blueprint(auth)
# Get database access from env.py
app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
# Set session type to filesystem
app.config['SESSION_TYPE'] = 'redis'
app.config['SESSION_PERMANENT'] = False
app.config['SESSION_USE_SIGNER'] = True
app.config['SESSION_REDIS'] = redis.from_url(
    os.environ.get("REDIS_URL"), health_check_interval=30)
# Get secret key from env.py
app.secret_key = os.environ.get("SECRET_KEY")
# Initiate PyMongo
mongo.init_app(app)
# Initiate Flask Session (server-side)
sess = Session(app)


@app.route("/")
def home():
    return redirect(url_for("movies.display_movies"))


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=False)
