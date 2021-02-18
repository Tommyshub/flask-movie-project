from flask import (Flask, flash, 
Blueprint, render_template, 
request, redirect, 
url_for, Response, 
session, abort)
import requests
import tmdbsimple as tmdb, requests
from forms import SearchForm, MovieForm
from bson.objectid import ObjectId
from database import mongo
import os
if os.path.exists("env.py"):
    import env

# Blueprint for this file
movie_search = Blueprint("movie_search", 
__name__, static_folder="static", template_folder="templates")
# Get api key from env.py
tmdb.API_KEY = os.environ.get("TMDB_KEY")
# Default language for imports 
tmdb.language = "en"
# Request session
tmdb.REQUESTS_SESSION = requests.Session()

search = tmdb.Search()

@movie_search.route("/home", methods=["POST", "GET"])
def home():
    # Fetch all information about all movies from the movies database in order to display it in the html
    home_movies = mongo.db.movies.find({}, {'movie_id': 1, 
    'movie_title': 1, 'movie_overview': 1, 'poster_path': 1, '_id': 0})
    form = SearchForm()
    if form.validate_on_submit():
       
        # Setting user input to string
        string = request.form["search"]
        
        # Display what user is searching for
        flash(f"Searching for {string}...")
       
        # Search for movie with user input from html form
        movies = search.movie(query=string)
        form.search.data = ""      
        return render_template('home.html', movies=movies, 
        search=search, home_movies=list(home_movies), form=form)
    return render_template('home.html', 
    search=search, home_movies=list(home_movies), form=form)


@movie_search.route("/review/<movie_id>", methods=["POST", "GET"])
def review(movie_id):
    form = MovieForm()
    
    #  Get current user for review info
    user = mongo.db.users.find_one(
    {"username": session["user"]})["username"].capitalize()
    
    # Connection to the movie database
    movie = tmdb.Movies(movie_id)
    response = movie.info()
    
    # Create veriables for title, overview and post path.
    movie_title = movie.title
    movie_id = movie.id
    movie_overview = movie.overview
    poster_path = movie.poster_path
    
    # Information about all movies that will be sent to the review page
    reviews = list(mongo.db.reviews.find({}, {'movie_id': 1, 
    'movie_title': 1, 'username': 1, 'review_text': 1, '_id': 1}))
    
    # Review information to send to the database
    review_info = {
        "movie_id": movie_id,
        "movie_title": movie.title,
        "username": user,
        "review_text": request.form.get("review")
    }
    # Information about the movie to send to the database
    movie_info = {
        "movie_id": movie_id,
        "movie_title": movie_title,
        "movie_overview": movie_overview,
        "poster_path": poster_path
    }
    
    if form.review.data and request.method == 'POST':
            mongo.db.reviews.insert_one(review_info)
            mongo.db.movies.insert_one(movie_info)
        
    
    return render_template('review.html', form=form, reviews=reviews, 
    movie_id=movie_id, movie_title=movie_title, 
    movie_overview=movie_overview, poster_path=poster_path, user=user)


@movie_search.route("/edit_review/<review_id>", methods=["GET","POST"])
def edit_review(review_id):
    
    # Fetch Object ID for editing
    review = mongo.db.reviews.find_one({"_id": ObjectId(review_id)})
    
    if request.method == "POST":
    # Data to send back
        submit = {
            "movie_id": review['movie_id'],
            "movie_title":  review['movie_title'],
            "username": review['username'],
            "review_text": request.form.get("review")
        }
        # Update objectid with submitted data
        mongo.db.reviews.update({"_id": ObjectId(review_id)},submit)
        flash("Review updated!")
    return render_template("edit_review.html", review=review)

@movie_search.route("/delete_review/<review_id>")
def delete(review_id):
    # Remove object connected to this objectid (review id)
    mongo.db.reviews.remove({"_id": ObjectId(review_id)})
    flash("Review succesfully deleted!")
    return redirect(url_for("auth.profile", username=session["user"]))