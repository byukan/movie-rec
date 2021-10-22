from flask import Flask, render_template ## request, session
from mov_rec import app
from mov_rec.models import User


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

@app.route('/signup', methods=['POST'])
def signup1():
    return User().signup()
