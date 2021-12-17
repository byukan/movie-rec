# this file is to consolidate all database interactions:
# use any below defined method to interact with the database (currently a stub)


from mov_rec import db
from flask import request, Response
import json
import random
import ast
from bson.objectid import ObjectId


def add_user(user):  # no longer relevant
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


def set_next_id():
    return random.randint(0, 999)


def find_movie(id):
    return db.movies.find_one({'_id': id})


def similar_movies(movie_id):
    try:
        db_response = db.similar_movies.find_one({'_id': movie_id}, {'_id': 0})

        if db_response:
            most_similar_movies = ast.literal_eval(db_response["similarity_scores"])
            return most_similar_movies  # this is of the form [ (id, score), (id, score) .... ]

    except Exception as ex:
        print(ex)

    return None


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
    
    return result, set_next_id()


def search_movies(search_term):
    movies = []

    try:
        # Full text search using search term, generating relevance score
        # Rank by relevance, then rating, then sort by title
        # Take the first 9

        to_search = {'$text': {'$search': search_term}}
        relevance_score = {'score': {'$meta': 'textScore'}}
        sort_criteria = [('score', {'$meta': 'textScore'}), ('IMDB_Rating', -1), ('Series_Title', 1)]

        movies = list(db.movies.find(to_search, relevance_score).sort(sort_criteria).limit(9))

    except Exception as ex:
        print(ex)

    return movies


# Sort by highest rating, then title, and take the first 9
def highest_rated_movies():
    sort_criteria = [('IMDB_Rating', -1), ('Series_Title', 1)]
    movies = list(db.movies.find({}).sort(sort_criteria).limit(9))
    return movies
