from flask import Flask, flash, Blueprint, render_template, request, redirect, url_for, Response, abort
import requests
from tmdbv3api import TMDb, Movie
from forms import SearchForm, SaveForm
from tmdb_key import TMDB_KEY
from bson.objectid import ObjectId
from database import mongo
import copy

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
# Html status codes 
r = requests.get('https://httpbin.org/get')


movie_id = ""
title = ""
overview = ""
poster_path = ""

# Route for search page 
@movie_search.route("/search", methods=["POST", "GET"])
def search():
    form = SearchForm()
    if form.validate_on_submit() and r.status_code == 200:
        string = request.form["search"]
        flash(f"Searching for {string}...")
        # Search for movie with variable from form
        movie_results = movie.search(string)
        movies = copy.deepcopy(movie_results)
        for key, value in movie_results[0].items():
            if key == "id":
                movie_id = copy.deepcopy(value)
            if key == "original_title":
                title = copy.deepcopy(value)
            if key == "overview":
                overview = copy.deepcopy(value)
            if key == "poster_path":
                poster_path = copy.deepcopy(value)
        return render_template('search.html', movies=movies, form=form)
    elif form.validate_on_submit() and r.status_code == 404:
        flash(f"No results found for {string}!")
    return render_template('search.html', form=form)


# Route for saving movie to database
@movie_search.route("/saved", methods=["POST", "GET"])
def save_movie():
    form = SaveForm()
    if form.validate_on_submit():
        mongo.db.movies.insert_one(movies)
        print(movies)
        flash(f"Movie {title} Saved!")
    return render_template('saved.html', form=form) 