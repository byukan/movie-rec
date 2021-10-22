from flask import Flask
from flask_pymongo import PyMongo

app = Flask(__name__)

try:
    mongo = pymongo.MongoClient(
        host="localhost", 
        port=27017, 
        serverSelectionTimeoutMS=3000)
    db = mongo.movie
    mongo.server_info() # if cannot connect to db, will get an exception
except:
    print("ERROR: Cannot connect to database")