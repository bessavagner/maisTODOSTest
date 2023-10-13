from flask_jwt_extended import create_access_token

from app.repositories.auth_repository import UserRepository
from app import bcrypt, jwt


class UserService:
    def __init__(self, user_repository: UserRepository, bcrypt: bcrypt, jwt: jwt):
        self.user_repository = user_repository
        self.bcrypt = bcrypt
        self.jwt = jwt

    def create_user(self, data):
        if 'email' not in data or 'password' not in data or 'confirm_password' not in data:
            raise ValueError("Incomplete data to create a user")

        existing_user = self.user_repository.get_user_by_email(data['email'])
        if existing_user:
            raise ValueError("Email already registered")

        if data['password'] != data['confirm_password']:
            raise ValueError("Password and confirm password do not match")

        hashed_password = self.bcrypt.generate_password_hash(data['password']).decode('utf-8')
        hashed_confirm_password = self.bcrypt.generate_password_hash(data['confirm_password']).decode('utf-8')

        del data['confirm_password']

        data['hashed_password'] = hashed_password
        data['hashed_confirm_password'] = hashed_confirm_password

        user = self.user_repository.create_user(data)

        return user

    def get_user_by_email(self, email):
        return self.user_repository.get_user_by_email(email)

    def generate_access_token(self, user):
        access_token = create_access_token(identity=user.id)
        return access_token
