from flask import Flask, render_template, request ##, session
from mov_rec import app
from mov_rec.models import User


@app.route("/")
@app.route("/home")
def home():
    return render_template ('home.html')

@app.route("/login")
def login():
    return render_template ('login.html')

@app.route("/signup/", methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        return User().signup()
    return render_template ('signup.html')
