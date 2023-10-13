from app.models.user import User
from app.repositories.auth_repository import UserRepository
from app import db


class SQLAlchemyUserRepository(UserRepository):
    def __init__(self, user: User):
        self.user = user

    def create_user(self, data):
        user = User(
            email=data['email'],
            password=data['hashed_password'],
            confirm_password=data['hashed_confirm_password']
        )
        db.session.add(user)
        db.session.commit()
        return user

    def get_user_by_email(self, email):
        return db.session.query(User).filter_by(email=email).first()
