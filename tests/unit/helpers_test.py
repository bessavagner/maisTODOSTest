import unittest
from unittest.mock import Mock, patch
import jwt
from app import app
from flask import jsonify


class TestTokenRequiredDecorator(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()

    @patch('jwt.decode')
    @patch('app.controllers.auth_controller.get_user_by_email')
    def test_valid_token(self, mock_get_user_by_email, mock_jwt_decode):
        mock_get_user_by_email.return_value = {'email': 'test@example.com', 'id': 1}
        mock_jwt_decode.return_value = {'username': 'test@example.com'}

        response = self.app.get('/api/v1/credit-card', headers={'Authorization': 'Bearer valid_token_here'})

        self.assertEqual(response.status_code, 200)

    @patch('jwt.decode', side_effect=jwt.ExpiredSignatureError)
    def test_expired_token(self, mock_jwt_decode):
        response = self.app.get('/api/v1/credit-card', headers={'Authorization': 'Bearer expired_token_here'})

        self.assertEqual(response.status_code, 401)

    @patch('jwt.decode', side_effect=jwt.InvalidTokenError)
    def test_invalid_token(self, mock_jwt_decode):
        response = self.app.get('/api/v1/credit-card', headers={'Authorization': 'Bearer invalid_token_here'})

        self.assertEqual(response.status_code, 401)

    def test_missing_token(self):
        response = self.app.get('/api/v1/credit-card')

        self.assertEqual(response.status_code, 401)


if __name__ == '__main__':
    unittest.main()
