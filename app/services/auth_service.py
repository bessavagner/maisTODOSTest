from flask_jwt_extended import create_access_token
from werkzeug.security import generate_password_hash
from app.repositories.auth_repository import UserRepository


class UserService:
    def __init__(self, user_repository: UserRepository):
        self.user_repository = user_repository

    def create_user(self, data):
        if 'email' not in data or 'password' not in data or 'confirm_password' not in data:
            raise ValueError("Incomplete data to create a user")

        existing_user = self.user_repository.get_user_by_email(data['email'])
        if existing_user:
            raise ValueError("Email already registered")

        if data['password'] != data['confirm_password']:
            raise ValueError("Password and confirm password do not match")

        hashed_password = generate_password_hash(data['password'])
        hashed_confirm_password = generate_password_hash(data['confirm_password'])

        del data['confirm_password']

        data['hashed_password'] = hashed_password
        data['hashed_confirm_password'] = hashed_confirm_password

        user = self.user_repository.create_user(data)

        return user

    def get_user_by_email(self, email):
        return self.user_repository.get_user_by_email(email)
