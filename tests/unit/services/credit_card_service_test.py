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


if __name__ == '__main__':
    unittest.main()
