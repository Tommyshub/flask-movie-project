from flask import Flask, flash, Blueprint, render_template, request, redirect, url_for, Response, abort
import requests
from tmdbv3api import TMDb, Movie
from forms import SearchForm, MovieForm
from bson.objectid import ObjectId
from database import mongo
import os
if os.path.exists("env.py"):
    import env

# Blueprint for this file
movie_search = Blueprint("movie_search", __name__, static_folder="static", template_folder="templates")
# Create an instance of TMDb
tmdb = TMDb()
# Create an instance of the movie functionn
movie = Movie()
# Get api key from env.py
tmdb.api_key = os.environ.get("TMDB_KEY")
# Default language for imports 
tmdb.language = "en"

@movie_search.route("/search", methods=["POST", "GET"])
def search():
    form = SearchForm()
    if form.validate_on_submit():
        # Setting user input to string
        string = request.form["search"]
        # Display what user is searching for
        flash(f"Searching for {string}...")
        # Search for movie with user input from html form
        movies = movie.search(string)
        return render_template('search.html', movies=movies, form=form)
    return render_template('search.html', form=form)


@movie_search.route("/create_review/<movie_id>", methods=["POST", "GET"])
def create_review(movie_id):
    form = MovieForm()
    # Create veriables for title, overview and post path. 
    movie_title = request.form["movie_title"]
    movie_overview = request.form["movie_overview"]
    poster_path = request.form["poster_path"]
    backdrop_path = request.form["backdrop_path"]
     # Check if the movie id already exists in db
    existing_movie = mongo.db.movies.find_one(
        {"movie_id": request.form.get("movie_id")})
    # If the user press create and if the movie does not exist in the database 
    if request.method == 'POST' and not existing_movie:
        # Insert movie id, title poster path and overview in the database
        mongo.db.movies.insert_one({'movie_id': request.form['movie_id'], 
                                    'movie_title': request.form['movie_title'],
                                    'poster_path': request.form['poster_path'],
                                    'movie_overview': request.form['movie_overview']})
        # If the user press create and if the movie exists in the database
    if request.method == 'POST' and existing_movie:
        print("Movie already exists in the database")

    return render_template('create_a_review.html', form=form, 
    movie_id=movie_id, movie_title=movie_title, movie_overview=movie_overview, poster_path=poster_path)
