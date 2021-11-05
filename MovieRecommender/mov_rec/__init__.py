from flask import Flask
from pymongo import MongoClient
from pymongo.errors import ConnectionFailure
from flask_bcrypt import Bcrypt


app = Flask(__name__)
bcrypt = Bcrypt(app)

try:
    mongodb_client = MongoClient(host='localhost', port=27017, connectTimeoutMS=5000)
    db = mongodb_client.stub
    mongodb_client.admin.command('ping') # if cannot connect to database, will get an exception
except ConnectionFailure:
    print("ERROR: Server unavailable")

from mov_rec import database, models, routes, search, view_movie