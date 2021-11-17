# this file is to consolidate all database interactions:
# use any below defined method to interact with the database (currently a stub)


from mov_rec import db
from flask import request, Response
import json
from bson.objectid import ObjectId


def add_user(user):
    try:
        
        dbResponse = db.users.insert_one(user)
        # for attr in dir(dbResponse):
        #     print(attr)
        print(dbResponse.inserted_id)
        
        return Response(
            response=json.dumps(
                {
                    "message": "user created", 
                    "id": f"{dbResponse.inserted_id}"
                }
            ), 
            status=200, 
            mimetype="application/json")
    except Exception as ex:
        print(ex)


def movie_info(movie_id):
    result = None

    try:
        # movie_count = db.movies.count_documents({})
        # print("movie count:", movie_count)

        # print("searching for movie with id:", movie_id)

        # results = list(db.movies.find({'_id': movie_id}))
        result = db.movies.find_one({'_id': movie_id})

        # if result:  # for result in results:
        #     for item in result:
        #         print(item + ":", result[item])

    except Exception as ex:
        print(ex)
    
    return result
