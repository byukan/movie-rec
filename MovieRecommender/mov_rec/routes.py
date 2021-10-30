from flask import Flask, render_template, request ##, session
from mov_rec import app, database
from mov_rec.models import User


@app.route("/")
@app.route("/home")
def home():
    print("app.debug=", app.debug, "from routes.py")
    # resp = database.test_create_user()
    # print(resp, "from module routes.py")
    return render_template ('home.html')

@app.route("/login")
def login():
    return render_template ('login.html')

@app.route("/signup/", methods=['GET', 'POST']) # 'POST' not implemented yet
def signup():
    if request.method == 'POST':
        print("you are here")
        return User().signup()
    return render_template ('signup.html') # method is 'GET'
