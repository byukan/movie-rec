from flask import Flask, render_template, request
from mov_rec import app, database


@app.route("/search/", methods=['GET', 'POST'])
def search():
    movies = []

    if request.method == 'POST':
        pass
        # search_term = request.args.get('')
        # results = db.movies.find(
        #     { $text: { $search: search_term }}, {score: { $meta: "textScore" }}
        # ).sort(
        #     {score: { $meta: "textScore" }}
        # )

    else:
        movies = database.highest_rated_movies()

    return render_template('search.html', movies=movies)
