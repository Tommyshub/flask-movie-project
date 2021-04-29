from flask import (Flask, flash,
                   Blueprint, render_template,
                   request, redirect,
                   url_for, Response,
                   session, abort)
import requests
import tmdbsimple as tmdb
import requests
from forms import ReviewForm
from bson.objectid import ObjectId
from database import mongo
import os
if os.path.exists("env.py"):
    import env

# Blueprint for this file
movies = Blueprint("movies",
                   __name__, static_folder="static",
                   template_folder="templates")
# Get api key from env.py
tmdb.API_KEY = os.environ.get("TMDB_KEY")
# Default language for imports
tmdb.language = "en"
# Connection to the database
tmdb.REQUESTS_SESSION = requests.Session()
# Search the movie database
search = tmdb.Search()


@movies.route("/movies", methods=["POST", "GET"])
def search_movies():
    """
    Fetch all information about all movies from the movies database 
    in order to display it in the html.
    """
    home_movies = mongo.db.movies.find({}, {'movie_id': 1,
                                            'movie_title': 1,
                                            'movie_overview': 1,
                                            'poster_path': 1,
                                            '_id': 0})
    form = ReviewForm()
    # Workaround to pop movie results from session on page reload
    if session.get('results') is not None:
        session.pop('results', None)
    if form.search.data and request.method == 'POST':
        # Setting user input to string
        string = request.form["search"]
        # Search for movie with user input from html form
        movies = search.movie(query=string)
        # Put movie search results in session
        session['results'] = movies['results']
        if movies['total_results'] == 0:
            # Clear search field on submit
            form.search.data = ""
            # Message that movie cannot be not found
            flash(f"No results found for {string}", "error")
        else:
            # Clear search field on submit
            form.search.data = ""
            # Message that results are displayed for movie
            flash(f"Display results for {string}", "success")
    return render_template('movies.html',
                           home_movies=list(home_movies), form=form)


@movies.route("/create/<movie_id>", methods=["POST", "GET"])
def create(movie_id):
    form = ReviewForm()
    # Connection to the movie database
    movie = tmdb.Movies(movie_id)
    response = movie.info()
    # Create veriables for title, overview and post path.
    movie_title = movie.title
    movie_id = movie.id
    movie_overview = movie.overview
    poster_path = movie.poster_path
    # Check if how many times the movie id exists in the database
    existing_movie = mongo.db.movies.find(
        {"movie_id": movie_id}, {'_id': 0}).count()
    # Information about the movie to send to the database
    movie_info = {
        "movie_id": movie_id,
        "movie_title": movie_title,
        "movie_overview": movie_overview,
        "poster_path": poster_path
    }

    if form.create.data and request.method == 'POST':
        # If the movie id exists less than 1 one time
        if existing_movie >= 1:
            flash("Redirected to existing review!", "info")
        # If the movie id does not exist in the database
        else:
            flash("Created Movie!", "success")
            # Insert movie information
            mongo.db.movies.insert_one(movie_info)
    return render_template('review.html', form=form,
                           movie_id=movie_id, movie_title=movie_title,
                           movie_overview=movie_overview,
                           poster_path=poster_path)


@movies.route("/review/<movie_id>", methods=["POST", "GET"])
def review(movie_id):
    form = ReviewForm()
    # Get current user for review info
    user = session["user"].capitalize()
    # Connection to the movie database
    movie = tmdb.Movies(movie_id)
    response = movie.info()
    # Create veriables for title, overview and post path.
    movie_title = movie.title
    movie_id = movie.id
    movie_overview = movie.overview
    poster_path = movie.poster_path
    # Information about movies that will be
    reviews = list(mongo.db.reviews.find({}, {'movie_id': 1,
                                              'movie_title': 1, 'username': 1,
                                              'review_text': 1, '_id': 1}))

    # Review information to send to the database
    review_info = {
        "movie_id": movie_id,
        "movie_title": movie.title,
        "username": user,
        "review_text": request.form.get("review")
    }

    if form.review.data and request.method == 'POST':
        mongo.db.reviews.insert_one(review_info)
        flash("Successfully posted your review", "success")
        return redirect(url_for("movies.review", movie_id=movie_id))
    return render_template('review.html', form=form,
                           reviews=reviews, movie_id=movie_id,
                           movie_title=movie_title,
                           movie_overview=movie_overview,
                           poster_path=poster_path, user=user)


@movies.route("/edit_review/<review_id>", methods=["GET", "POST"])
def edit_review(review_id):
    # Fetch ObjectID info from database and pass it to submit
    review = mongo.db.reviews.find_one({"_id": ObjectId(review_id)})
    if request.method == "POST":
        # Get info from database and form for editing
        submit = {
            "movie_id": review['movie_id'],
            "movie_title":  review['movie_title'],
            "username": review['username'],
            "review_text": request.form.get("edit-review")
        }
        # Update objectid with submitted data
        mongo.db.reviews.update({"_id": ObjectId(review_id)}, submit)
        flash("Review updated!", "success")
        return redirect(url_for("auth.profile", username=session["user"]))
    return render_template("edit_review.html", review=review)


@movies.route("/delete_review/<review_id>")
def delete(review_id):
    # Remove object connected to this objectid (review id)
    mongo.db.reviews.remove({"_id": ObjectId(review_id)})
    flash("Review succesfully deleted!", "success")
    return redirect(url_for("auth.profile", username=session["user"]))
