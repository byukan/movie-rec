from flask import Flask
from MovRec import app
from user.models import User

@app.route('/signup', methods=['POST'])
def signup1():
  return User().signup()

