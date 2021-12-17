from flask import Flask, request
from mov_rec import app, database
from mov_rec.view_function_response import ViewFunctionResponse


@app.route("/", methods=['GET', 'POST'])
@app.route("/home/", methods=['GET', 'POST'])
def search():  # wrapper for view function, to allow for testing
    view_response = search_response(request)
    return view_response.get_http_response()


def search_response(request):
    view_response = ViewFunctionResponse()

    if request.method == 'POST':
        search_term = request.form["search_term"]
        movies = database.search_movies(search_term)

    else:
        movies = database.highest_rated_movies()

    kwargs = {'movies': movies}
    view_response.create_render_response('home.html', kwargs)
    return view_response
