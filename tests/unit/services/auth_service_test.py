import unittest
from unittest.mock import Mock
from app.services.auth_service import UserService
from app.repositories.auth_repository import UserRepository


class TestUserService(unittest.TestCase):
    def setUp(self):
        self.user_repository = Mock()
        self.user_service = UserService(self.user_repository)

    def test_create_user_success(self):
        self.user_repository.get_user_by_email.return_value = None
        self.user_repository.create_user.return_value = {'id': 1, 'email': 'luan@test.com'}

        result = self.user_service.create_user({'email': 'luan@test.com', 'password': 'password', 'confirm_password': 'password'})

        self.assertEqual(result, {'id': 1, 'email': 'luan@test.com'})

    def test_create_user_incomplete_data(self):
        incomplete_data = {
            'email': 'test@example.com',
            'password': 'password123'
        }
        with self.assertRaises(ValueError):
            self.user_service.create_user(incomplete_data)

    def test_create_user_existing_email(self):
        existing_email = {
            'email': 'test@example.com',
            'password': 'password123',
            'confirm_password': 'password123'
        }
        self.user_repository.get_user_by_email = Mock(return_value=existing_email)
        with self.assertRaises(ValueError):
            self.user_service.create_user(existing_email)

    def test_create_user_password_mismatch(self):
        password_mismatch = {
            'email': 'test@example.com',
            'password': 'password123',
            'confirm_password': 'password456'
        }
        with self.assertRaises(ValueError):
            self.user_service.create_user(password_mismatch)

    def test_get_user_by_email(self):
        self.user_repository.get_user_by_email.return_value = None

        email = 'user@example.com'
        user = self.user_service.get_user_by_email(email)

        self.assertIsNone(user)


if __name__ == '__main__':
    unittest.main()
