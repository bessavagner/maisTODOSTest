# controllers/auth_controller.py
import datetime
from flask import request, jsonify
from app import app
from app.repositories.sql_auth_repository import SQLAlchemyUserRepository
from app.services.auth_service import UserService
from app.models.user import User
import jwt
from werkzeug.security import check_password_hash

user_repository = SQLAlchemyUserRepository(User)
user_service = UserService(user_repository)


def register():
    data = request.get_json()

    if 'email' in data and 'password' in data and 'confirm_password' in data:
        user = user_service.create_user(data)
        if user:
            return jsonify({"message": "User registered successfully"}), 201
        else:
            return jsonify({"message": "Failed to register user"}), 500
    else:
        return jsonify({"message": "Email and password are required"}), 400


def login():
    data = request.get_json()

    if 'email' in data and 'password' in data:
        user = user_service.get_user_by_email(data['email'])
        if user and check_password_hash(user['password'], data['password']):
            token = jwt.encode(
                {'username': user['email'], 'exp': datetime.datetime.now() + datetime.timedelta(hours=12)},
                app.config['SECRET_KEY'])
            return jsonify({'message': 'Validated successfully', 'token': token,
                            'exp': datetime.datetime.now() + datetime.timedelta(hours=1)})
        else:
            return jsonify({"message": "Invalid email or password"}), 401
    else:
        return jsonify({"message": "Email and password are required"}), 400


def get_user_by_email(username):
    user = user_service.get_user_by_email(username)

    if user:
        return jsonify(user), 200
    else:
        return jsonify({"message": "User not found"}), 404
