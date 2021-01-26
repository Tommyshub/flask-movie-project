from flask import Blueprint, render_template
from tmdb3 import searchMovie


tmdb = Blueprint("tmdb", __name__, static_folder="static", template_folder="templates")


