from flask import Flask, flash, Blueprint, render_template, request, redirect, url_for
from tmdbv3api import TMDb, Movie
from forms import SearchForm
from tmdb_key import TMDB_KEY

# Blueprint for this file
movie_search = Blueprint("movie_search", __name__, static_folder="static", template_folder="templates")

# Create an instance of TMDb
tmdb = TMDb()
# Create an instance of the movie functionn
movie = Movie()
# Set API key
tmdb.api_key = TMDB_KEY
# Default language for imports 
tmdb.language = "en"


# Route for search page 
@movie_search.route("/search", methods=["POST", "GET"])
def search():
    form = SearchForm()
    if request.method == "POST":
        string = request.form["search"]
        flash(f"Searching for {string}...")
        # Search for movie with variable from form
        movies = movie.search(string)
        return render_template('search.html', movies=movies, form=form)
    
    return render_template('search.html', form=form)


