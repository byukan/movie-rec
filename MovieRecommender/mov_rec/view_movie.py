from flask import Flask, render_template, request
from mov_rec import app, database


@app.route("/view_movie", methods=['GET', 'POST']) # POST is for liking or favoriting a movie; not implemented yet
def view_movie():
    movie_id = request.args.get('id') # picks up url parameter

    # print("getting movie info for movie_id:", movie_id, ", from module view_movie.py")
    movie = database.movie_info(movie_id)

    if movie:
        print("Movie retrieved:", movie)
    else:
        print("No movie found")

    return render_template('view_movie.html', movie=movie)
