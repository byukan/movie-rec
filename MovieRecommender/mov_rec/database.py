# this file is to consolidate all database interactions:
# use any below defined method to interact with the database (currently a stub)


from mov_rec import db
from flask import request, Response
import json
import random
import ast
from bson.objectid import ObjectId


def add_user(user):
    user_id = None
    try:
        
        db_response = db.users.insert_one(user)
        # for attr in dir(dbResponse):
        #     print(attr)
        print(db_response.inserted_id)

        user_id = str(db_response.inserted_id)

    except Exception as ex:
        print(ex)

    return user_id


def _set_next_id():
    return random.randint(0, 999)


def find_movie(id):
    return db.movies.find_one({'_id': id})


def movie_info(movie_id, is_main=False):

    result = None

    try:
        result = find_movie(movie_id)

        if result:

            # add suggestions if needed
            if is_main:
                result["Suggestions"] = []
                similar_movie_ids = similar_movies(movie_id)[1:]

                for similar in similar_movie_ids:
                    id = similar[0]
                    similar_info, _ = movie_info(id)
                    result["Suggestions"].append(similar_info)

    except Exception as ex:
        print(ex)
    
    return result, _set_next_id()


def similar_movies(movie_id):
    try:
        db_response = db.similar_movies.find_one({'_id': movie_id}, {'_id': 0})

        if db_response:
            most_similar_movies = ast.literal_eval(db_response["similarity_scores"])
            return most_similar_movies

    except Exception as ex:
        print(ex)

    return None


def search_movies(search_term):
    movies = []

    try:
        # Full text search using search term
        # Sort results by relevance, then rating, then title
        # Take the first 9
        movies = list(
            db.movies.find({'$text': {'$search': search_term}}, {'score': {'$meta': 'textScore'}}).sort([('score', {'$meta': 'textScore'}), ('IMDB_Rating', -1), ('Series_Title', 1)]).limit(9))

    except Exception as ex:
        print(ex)

    return movies


def highest_rated_movies():
    # First sort all the docs by rating, and take the first 9
    movies = list(db.movies.find({}).sort([('IMDB_Rating', -1), ('Series_Title', 1)]).limit(9))
    return movies
