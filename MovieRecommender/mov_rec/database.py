# this file is to consolidate all database interactions:
# use any below defined method to interact with the database (currently a stub)


from mov_rec import db
from flask import request, Response
import json
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


def movie_info(movie_id):
    result = None

    try:
        # movie_count = db.movies.count_documents({})
        # print("movie count:", movie_count)
        # print("searching for movie with id:", movie_id)

        # results = list(db.movies.find({'_id': movie_id}))
        result = db.movies.find_one({'_id': movie_id})

        # hardcoded similar movies
        if result:
            result["similar_movies"] = [
                {
                    '_id': 502,
                    'Series_Title': "Iron Man",
                    'Poster_Link': 'https://m.media-amazon.com/images/M/MV5BMTczNTI2ODUwOF5BMl5BanBnXkFtZTcwMTU0NTIzMw@@.jpg'
                },
                {
                    '_id': 103,
                    'Series_Title': "Reservoir Dogs",
                    'Poster_Link': 'https://m.media-amazon.com/images/M/MV5BZmExNmEwYWItYmQzOS00YjA5LTk2MjktZjEyZDE1Y2QxNjA1XkEyXkFqcGdeQXVyMTQxNzMzNDI@.jpg'
                },
                {
                    '_id': 900,
                    'Series_Title': "The Raid",
                    'Poster_Link': 'https://m.media-amazon.com/images/M/MV5BZGIxODNjM2YtZjA5Mi00MjA5LTk2YjItODE0OWI5NThjNTBmXkEyXkFqcGdeQXVyNzQ1ODk3MTQ@.jpg'
                }
            ]

    except Exception as ex:
        print(ex)
    
    return result
