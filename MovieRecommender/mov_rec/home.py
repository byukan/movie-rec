from flask import Flask, render_template, request
from mov_rec import app, database

@app.route("/", methods=['GET', 'POST'])
@app.route("/home/", methods=['GET', 'POST'])
def search():
    print("Request method:", request.method)

    if request.method == 'GET' or not request.form["search_term"]:  # want to ignore ""
        movies = database.highest_rated_movies()

    else:  # method is POST with a search term
        search_term = request.form["search_term"]
        print("Search term:", search_term)
        movies = database.search_movies(search_term)

    return render_template('home.html', movies=movies)
