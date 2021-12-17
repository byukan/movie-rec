from flask import Flask, request
from mov_rec import app, database
from mov_rec.view_function_response import ViewFunctionResponse


@app.route("/view_movie", methods=['GET'])
def view_movie():  # wrapper for view function, to allow for testing
    view_response = view_movie_response(request)
    return view_response.get_http_response()


def view_movie_response(request):
    view_response = ViewFunctionResponse()

    movie_id = -1
    movie_id_string = request.args.get('id')  # if no ID parameter, movie_id_string will be None
    if movie_id_string:
        movie_id = int(movie_id_string)

    movie, next_id = database.movie_info(movie_id, True)
    kwargs = {'movie': movie, 'next_id': next_id}
    view_response.create_render_response('view_movie.html', kwargs)
    return view_response
