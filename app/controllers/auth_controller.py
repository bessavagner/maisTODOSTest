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


@app.route('/api/v1/register', methods=['POST'])
def register():
    """
    Register a new user.

    ---
    tags:
      - Authentication
    parameters:
      - name: data
        in: body
        required: true
        schema:
          type: object
          properties:
            email:
              type: string
            password:
              type: string
            confirm_password:
              type: string
    responses:
      201:
        description: User registered successfully.
      400:
        description: Invalid request data.
      500:
        description: Failed to register user.
    """
    data = request.get_json()

    app.logger.info('AuthController - register - validate payload')
    if 'email' in data and 'password' in data and 'confirm_password' in data:
        app.logger.info('AuthController - register - checking email size')
        if len(data['email']) > 255:
            return jsonify({"message": "Email is too long"}), 400

        app.logger.info('AuthController - register - checking password size')
        if len(data['password']) < 8:
            return jsonify({"message": "Password is too short"}), 400

        app.logger.info('AuthController - register - call service to create new user')
        user = user_service.create_user(data)
        if user:
            app.logger.info('AuthController - register - user created')
            return jsonify({"message": "User registered successfully"}), 201
        else:
            app.logger.error('AuthController - register - error to register user')
            return jsonify({"message": "Failed to register user"}), 500
    else:
        app.logger.error('AuthController - register - payload validation error')
        return jsonify({"message": "Email and password are required"}), 400


@app.route('/api/v1/login', methods=['POST'])
def login():
    """
    Log in and obtain an authentication token.

    ---
    tags:
      - Authentication
    parameters:
      - name: data
        in: body
        required: true
        schema:
          type: object
          properties:
            email:
              type: string
            password:
              type: string
    responses:
      200:
        description: Validated successfully.
        schema:
          type: object
          properties:
            message:
              type: string
            token:
              type: string
            exp:
              type: string
      401:
        description: Unauthorized.
    """
    data = request.get_json()

    app.logger.info('AuthController - login - validate payload')
    if 'email' in data and 'password' in data:
        app.logger.info('AuthController - login - get user by email')
        user = user_service.get_user_by_email(data['email'])

        app.logger.info('AuthController - login - validate match passwords')
        if user and check_password_hash(user['password'], data['password']):

            app.logger.info('AuthController - login - generate token with expiration date')
            token = jwt.encode(
                {'username': user['email'], 'exp': datetime.datetime.now() + datetime.timedelta(hours=12)},
                app.config['SECRET_KEY'])
            return jsonify({'message': 'Validated successfully', 'token': token,
                            'exp': datetime.datetime.now() + datetime.timedelta(hours=1)})
        else:
            app.logger.error('AuthController - login - Login error')
            return jsonify({"message": "Invalid email or password"}), 401
    else:
        app.logger.error('AuthController - login - payload validation error')
        return jsonify({"message": "Email and password are required"}), 400


@app.route('/api/v1/user/<string:username>', methods=['GET'])
def get_user_by_email(username):
    """
    Get user information by email.

    ---
    tags:
      - Authentication
    parameters:
      - name: username
        in: path
        required: true
        type: string
        description: User's email.
    responses:
      200:
        description: User details.
        schema:
          type: object
          properties:
            user_id:
              type: integer
            email:
              type: string
            # Add other user properties here
      404:
        description: User not found.
    """
    app.logger.info('AuthController - getUserByEmail - call service method')
    user = user_service.get_user_by_email(username)

    if user:
        app.logger.info('AuthController - getUserByEmail - return found user by email')
        return jsonify(user), 200
    else:
        app.logger.error('AuthController - getUserByEmail - user not found')
        return jsonify({"message": "User not found"}), 404
