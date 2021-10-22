from flask import Flask, jsonify, request
from passlib.hash import pbkdf2_sha256
from MovRec import db
import uuid

class User:
    def signup(self):
        print(request.form)

        user = {
            "-id": uuid.uuid4().hex,
            "name": request.form.get('name'),
            "email": request.form.get('email'),
            "password": request.form.get('password')
        }

        # Encrypt the password
        user['password'] = pbkdf2_sha256.hash(user['password'])
          #Check for the existing email add             if db.users.find_one({"email": user['email']}):
            # return jsonify({"error": "Email address already in use"}), 400
        if db.users.insert_one(user):
            return jsonify(user), 200

        
        return jsonify({"error": "Signup failed"}), 400



