import unittest
from unittest.mock import Mock
from app.services.credit_card_service import CreditCardService


class TestCreditCardService(unittest.TestCase):

    def setUp(self):
        self.repository = Mock()
        self.service = CreditCardService(self.repository)

    def test_list_credit_cards(self):
        self.repository.list_credit_cards.return_value = [{'id': 1, 'number': '1234'}, {'id': 2, 'number': '5678'}]
        result = self.service.list_credit_cards()
        self.assertEqual(result, [{'id': 1, 'number': '1234'}, {'id': 2, 'number': '5678'}])

    def test_get_credit_card(self):
        key = 1
        self.repository.get_credit_card.return_value = {'id': key, 'number': '1234'}
        result = self.service.get_credit_card(key)
        self.assertEqual(result, {'id': key, 'number': '1234'})

    def test_create_credit_card_valid(self):
        valid_payload = {
            "exp_date": "02/2024",
            "holder": "Samara Holanda",
            "number": "4005519200000004",
            "cvv": "123"
        }

        self.repository.create_credit_card.return_value = valid_payload

        result, status_code = self.service.create_credit_card(valid_payload)
        self.assertEqual(status_code, 201)
        self.assertEqual(result, valid_payload)

    def test_create_credit_card_invalid_number(self):
        invalid_payload = {
            "number": "1234",
            "holder": "Luan Santos",
            "exp_date": "12/25",
            "cvv": "123"
        }

        result, status_code = self.service.create_credit_card(invalid_payload)
        self.assertEqual(status_code, 422)

    def test_create_credit_card_missing_data(self):
        missing_data_payload = {
            "holder": "Luan Santos",
            "exp_date": "12/25",
            "cvv": "123"
        }

        result, status_code = self.service.create_credit_card(missing_data_payload)
        self.assertEqual(status_code, 400)

    def test_create_credit_card_invalid_exp_date(self):
        invalid_exp_date_payload = {
            "number": "4111111111111111",
            "holder": "Luan Santos",
            "exp_date": "25-12-2024",
            "cvv": "123"
        }

        result, status_code = self.service.create_credit_card(invalid_exp_date_payload)
        self.assertEqual(status_code, 400)

    def test_create_credit_card_existing_card(self):
        existing_card_payload = {
            "number": "4111111111111111",
            "holder": "Luan Santos",
            "exp_date": "12/25",
            "cvv": "123"
        }

        self.repository.get_credit_card_by_number.return_value = existing_card_payload

        result, status_code = self.service.create_credit_card(existing_card_payload)
        self.assertEqual(status_code, 400)


if __name__ == '__main__':
    unittest.main()
