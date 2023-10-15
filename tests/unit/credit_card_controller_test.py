import unittest

from flask import Flask
from flask_testing import TestCase
from app.controllers import credit_card_controller


class CreditCardControllerTest(TestCase):
    def create_app(self):
        app = Flask(__name__)
        app.config['TESTING'] = True
        return app

    def test_list_credit_cards(self):
        response = self.app.get('/api/v1/credit-card')
        self.assertEqual(response.status_code, 200)

    def test_get_credit_card(self):
        response = self.app.get('/api/v1/credit-card/1')
        self.assertEqual(response.status_code, 200)

    def test_get_credit_card_not_found(self):
        response = self.app.get('/api/v1/credit-card/999')
        self.assertEqual(response.status_code, 404)


if __name__ == '__main__':
    unittest.main()
