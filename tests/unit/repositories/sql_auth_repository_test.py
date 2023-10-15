import unittest
from unittest.mock import patch
from app.repositories.sql_auth_repository import SQLAlchemyUserRepository
from app.models.user import User
from app import db, app


class TestSQLAlchemyUserRepository(unittest.TestCase):
    def setUp(self):
        self.user_repository = SQLAlchemyUserRepository(User)

    def test_create_user(self):
        with app.app_context():
            with patch('app.repositories.sql_auth_repository.db.session.commit') as commit_mock:
                user_data = {'email': 'test@example.com', 'hashed_password': 'hashed_password',
                             'hashed_confirm_password': 'hashed_confirm_password'}
                user = self.user_repository.create_user(user_data)

                self.assertEqual(user.email, user_data['email'])
                self.assertEqual(user.password, user_data['hashed_password'])
                self.assertEqual(user.confirm_password, user_data['hashed_confirm_password'])
                commit_mock.assert_called_once()

    def test_get_user_by_email_existing_user(self):
        email = 'test@example.com'
        with app.app_context():
            with patch('app.repositories.sql_auth_repository.db.session.query') as query_mock:
                query_mock().filter().first.return_value = User(email=email)

                user = self.user_repository.get_user_by_email(email)

                self.assertEqual(user['email'], email)

    def test_get_user_by_email_non_existing_user(self):
        email = 'nonexistent@example.com'
        with app.app_context():
            with patch('app.repositories.sql_auth_repository.db.session.query') as query_mock:
                query_mock().filter().first.return_value = None

                user = self.user_repository.get_user_by_email(email)

                self.assertIsNone(user)


if __name__ == '__main__':
    unittest.main()
