from flask import Flask, jsonify, request
# from passlib.hash import pbkdf2_sha256
# from MovRec import db
from mov_rec import bcrypt, database
# import uuid


# consider not having a user class and methods
# rather: add this functionality to a login_register module instead
class User:
    def signup(self):
        print(request.form)

        # need to check for existing email first (not implemented yet)
        # return jsonify({"error": "Email address already in use"}), 400

        user = {
            'name': request.form["name"], 
            'email': request.form["email"], 
            "password_hash": User.hash_password(request.form["password"]) # encrypt password
        }

        print(user)
        database.add_user(user)
        return jsonify({"message": "Signing up"}), 200 # instead, render a different page
    
    @classmethod
    def hash_password(cls, password):
        return bcrypt.generate_password_hash(password).decode('utf-8')
