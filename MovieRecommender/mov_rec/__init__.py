from flask import Flask
from pymongo import MongoClient
from pymongo.errors import ConnectionFailure
import certifi


app = Flask(__name__)

try:
    ca = certifi.where()
    mongodb_client = MongoClient("mongodb+srv://m001-student:3@r.vu0ut.mongodb.net/movie?retryWrites=true&w=majority",
                                 tlsCAFile=ca, connectTimeoutMS=5000)
    db = mongodb_client.movie
    mongodb_client.admin.command('ping')  # if cannot connect to database, will get an exception
except ConnectionFailure:
    print("ERROR: Server unavailable")


from mov_rec import database, home, view_movie, view_function_response
