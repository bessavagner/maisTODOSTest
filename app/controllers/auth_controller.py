from flask import request, jsonify
from app import app, bcrypt, jwt
from app.repositories.sql_auth_repository import SQLAlchemyUserRepository
from app.services.auth_service import UserService
from app.models.user import User

user_repository = SQLAlchemyUserRepository(User)
user_service = UserService(user_repository, bcrypt, jwt)


@app.route('/api/v1/register', methods=['POST'])
def register():
    data = request.get_json()

    if 'email' in data and 'password' in data and 'confirm_password' in data:
        user = user_service.create_user(data)
        if user:
            return jsonify({"message": "User registered successfully"}, 201)
        else:
            return jsonify({"message": "Failed to register user"}, 400)
    else:
        return jsonify({"message": "Email and password are required"}, 400)


@app.route('/api/v1/login', methods=['POST'])
def login():
    data = request.get_json()

    if 'email' in data and 'password' in data:
        user = user_service.get_user_by_email(data['email'])
        if user and user_service.bcrypt.check_password_hash(user.password, data['password']):
            access_token = user_service.generate_access_token(user)
            return jsonify({"access_token": access_token}), 200
        else:
            return jsonify({"message": "Invalid email or password"}, 401)
    else:
        return jsonify({"message": "Email and password are required"}, 400)
