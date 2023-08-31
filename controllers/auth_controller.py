from flask import Blueprint, request, jsonify, session
from application import db
from werkzeug.security import generate_password_hash, check_password_hash

auth_controller = Blueprint('auth', __name__)

users_collection = db["users"]

@auth_controller.route("/login", methods=['POST'])
def login():
    data = request.json
    username = data['username']
    password = data['password']

    user = users_collection.find_one({"username": username})

    if not user or not check_password_hash(user["password"], password):
        return jsonify({"message": "Invalid username or password"}), 401

    session['user_id'] = str(user["_id"])

    return jsonify({"message": "Login successful"}), 200

@auth_controller.route("/register", methods=['POST'])
def register():
    data = request.json
    username = data['username']
    password = data['password']

    # Check if the username is already taken
    existing_user = users_collection.find_one({"username": username})
    if existing_user:
        return jsonify({"message": "Username already taken"}), 400

    # Hash the password
    hashed_password = generate_password_hash(password, method='sha256')

    new_user = {"username": username, "password": hashed_password}
    users_collection.insert_one(new_user)

    return jsonify({"message": "User registered successfully"}), 201

@auth_controller.route('/logout', methods=['POST'])
def logout():
    session.pop('user_id', None)
    return jsonify({"message": "Logged out"}), 200
