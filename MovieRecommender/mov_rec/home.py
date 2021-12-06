from flask import Flask, render_template, request
from mov_rec import app, database

@app.route("/", methods=['GET', 'POST'])
@app.route("/home/", methods=['GET', 'POST'])
def search():
    print("Request method:", request.method)

    if request.method == 'POST':
        search_term = request.form["search_term"]
        movies = database.search_movies(search_term)

    else:
        movies = database.highest_rated_movies()

    return render_template('home.html', movies=movies)
