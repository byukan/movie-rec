from flask import Flask, render_template, request
from mov_rec import app, database


@app.route("/view_movie", methods=['GET', 'POST'])  # POST is for liking or favoriting a movie; not implemented yet
def view_movie():
    movie_id = -1
    movie_id_string = request.args.get('id')  # if no ID parameter, movie_id_string will be None
    if movie_id_string:
        movie_id = int(movie_id_string)
    print('url param & id:', movie_id_string, movie_id)

    movie, next_id = database.movie_info(movie_id, True)
    return render_template('view_movie.html', movie=movie, next_id=next_id)
