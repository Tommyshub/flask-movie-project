from flask import Blueprint, render_template, abort, json
from flask_pymongo import PyMongo

# Blueprint for this file
database = Blueprint("database", __name__, 
static_folder="static", template_folder="templates/errors/")

# Creates instance of pymongo 
mongo = PyMongo()