from flask import Flask, flash, Blueprint, render_template, request, redirect, url_for, Response, session, abort
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

@movie_search.route("/home", methods=["POST", "GET"])
def home():
    # Fetch all information about all movies from the movies database in order to display it in the html
    home_movies = mongo.db.movies.find({}, {'movie_id': 1, 'movie_title': 1, 'movie_overview': 1, 'poster_path': 1, '_id': 0})
    form = SearchForm()
    if form.validate_on_submit():
        # Setting user input to string
        string = request.form["search"]
        # Display what user is searching for
        flash(f"Searching for {string}...")
        # Search for movie with user input from html form
        movies = movie.search(string)
        return render_template('home.html', movies=movies, home_movies=list(home_movies), form=form)
    return render_template('home.html', home_movies=list(home_movies), form=form)



@movie_search.route("/review/<movie_id>", methods=["POST", "GET"])
def review(movie_id):
    form = MovieForm()
    # Get currrent user 
    user = mongo.db.users.find_one(
    {"username": session["user"]})["username"].capitalize()
    # Create veriables for title, overview and post path. 
    movie = mongo.db.movies.find_one({"movie_id": movie_id})
    movie_title = movie['movie_title']
    movie_overview = movie['movie_overview']
    poster_path = movie['poster_path']
    # Information about the review to send to the database 
    review_info = {
        "movie_id": movie_id,
        "username": user,
        "review_text": request.form.get("review")
    }
    # If the user press create and if the movie does not exist in the database 
    if request.method == 'POST' and not movie:
        # Insert movie id, title poster path and overview in the database
        mongo.db.movies.insert_one({'movie_id': request.form['movie_id'], 
                                    'movie_title': request.form['movie_title'],
                                    'poster_path': request.form['poster_path'],
                                    'movie_overview': request.form['movie_overview']})
    # Send information from the review form to the database 
    if request.method == 'POST':
        mongo.db.reviews.insert_one(review_info)
        print(review_info)
    return render_template('review.html', form=form, 
    movie_id=movie_id, movie_title=movie_title, movie_overview=movie_overview, poster_path=poster_path)