from flask import Flask, render_template, request, session
import pymongo


app = Flask(__name__)  

client = pymongo.MongoClient('localhost', 27017)
db= client.user_login_system

from user import routes

@app.route("/")
@app.route("/home")
def home():
    return render_template ('home.html')

@app.route("/login")
def login():
    
    return render_template ('login.html')

@app.route("/signup")
def signup():
    return render_template ('signup.html')

if __name__ == "__main__":
    app.run(debug=True)
