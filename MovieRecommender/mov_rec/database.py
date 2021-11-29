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


def movie_info(movie_id): # not currently working
    try:
        movie_count = db.movies.count_documents({})
        print("movie count:", movie_count)

        results = list(db.movies.find({'id': movie_id }))
        # results = list(db.movies.find({'id': f"{movie_id}" }))
        print(results)

        for result in results:
            result["_id"] = str(result["_id"])
            print(result["_id"], result["title"])
        
        # for attr in dir(dbResponse):
        #     print(attr)

        return Response(
            response=json.dumps(results), 
            status=200, 
            mimetype="application/json")
    except Exception as ex:
        print(ex)
    
    return None
