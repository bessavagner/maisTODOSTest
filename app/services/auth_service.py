from flask_jwt_extended import create_access_token
from werkzeug.security import generate_password_hash
from app import app
from app.repositories.auth_repository import UserRepository


class UserService:
    def __init__(self, user_repository: UserRepository):
        self.user_repository = user_repository

    def create_user(self, data):
        app.logger.info('AuthService - createUser - validate payload')
        if 'email' not in data or 'password' not in data or 'confirm_password' not in data:
            raise ValueError("Incomplete data to create a user")

        app.logger.info('AuthService - createUser - verify if exists user by email')
        existing_user = self.user_repository.get_user_by_email(data['email'])
        if existing_user:
            app.logger.error('AuthService - createUser - user is in database')
            raise ValueError("Email already registered")

        if data['password'] != data['confirm_password']:
            app.logger.error('AuthService - createUser - password validation failed')
            raise ValueError("Password and confirm password do not match")

        app.logger.info('AuthService - createUser - hash password and password confirmation')
        hashed_password = generate_password_hash(data['password'])
        hashed_confirm_password = generate_password_hash(data['confirm_password'])

        del data['confirm_password']

        app.logger.info('AuthService - createUser - hash values passed in data')
        data['hashed_password'] = hashed_password
        data['hashed_confirm_password'] = hashed_confirm_password

        app.logger.info('AuthService - createUser - call repository to create user')
        user = self.user_repository.create_user(data)

        app.logger.info('AuthService - createUser - return created user')
        return user

    def get_user_by_email(self, email):
        app.logger.info(f'AuthService - createUser - call repository to find user by email: {email}')
        return self.user_repository.get_user_by_email(email)
