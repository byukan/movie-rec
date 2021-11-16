from flask import Flask, render_template, request ##, session
from mov_rec import app, database
from mov_rec.models import User


@app.route("/")
@app.route("/home")
def home():
    _print_debug_statement("app.debug=", app.debug, "routes")
    # resp = database.test_create_user()
    # resp = database.movie_info(1)
    # _print_debug_statement("", resp, "routes")
    return render_template ('home.html')


@app.route("/login/") # not yet implemented
def login():
    return render_template ('login.html')


@app.route("/signup/", methods=['GET', 'POST']) # POST not completely implemented
def signup():
    if request.method == 'POST':
        return User().signup()
    return render_template ('signup.html') # method is 'GET'


@app.route("/usersfeed/")
def usersfeed():
    return render_template ('usersfeed.html')


def _print_debug_statement(description, element, module):
    if app.debug:
        print(description, element, ", from module " + module + ".py")

