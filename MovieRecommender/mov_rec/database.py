# this file is to consolidate all database interactions:
# use any below defined method to interact with the database (currently a stub)


from mov_rec import db
from flask import Response
import json


def test_create_user():
    try:
        user = {'first_name': "Guido", 'last_name': "van Rossum", 'age': 65}
        
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
    try:
        dbResponse = db.movies.find({'id': movie_id })
        for attr in dir(dbResponse):
            print(attr)
        
        return Response(
            response=json.dumps(
                {
                    "message": f"movie info for movie_id {movie_id}"
                }
            ), 
            status=200, 
            mimetype="application/json")
    except Exception as ex:
        print(ex)
    
    return None
