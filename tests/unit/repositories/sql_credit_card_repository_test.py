import unittest
from unittest.mock import patch
from app.models.credit_card import CreditCard
from app.repositories.sql_credit_card_repository import SQLCreditCardRepository
from app import db, app


class TestSQLCreditCardRepository(unittest.TestCase):
    def setUp(self):
        self.credit_card_repository = SQLCreditCardRepository(CreditCard)

    def test_list_credit_cards(self):
        with app.app_context():
            with patch('app.repositories.sql_credit_card_repository.db.session.query') as query_mock:
                expected_credit_cards = [
                    CreditCard(exp_date='01/23', holder='Luan Santos', number='1234567812345678', cvv='123', brand='Visa'),
                    CreditCard(exp_date='02/24', holder='Samara Holanda', number='8765432187654321', cvv='456',
                               brand='MasterCard')
                ]
                query_mock().all.return_value = expected_credit_cards

                credit_cards = self.credit_card_repository.list_credit_cards()

                self.assertEqual(credit_cards, expected_credit_cards)

    def test_get_credit_card_existing_card(self):
        card_id = 1
        with app.app_context():
            with patch('app.repositories.sql_credit_card_repository.db.session.query') as query_mock:
                expected_credit_card = CreditCard(exp_date='01/23', holder='Luan Santos', number='1234567812345678',
                                                  cvv='123', brand='Visa')
                query_mock().filter().first.return_value = expected_credit_card

                credit_card = self.credit_card_repository.get_credit_card(card_id)

                self.assertEqual(credit_card, expected_credit_card.to_dict())

    def test_get_credit_card_non_existing_card(self):
        card_id = 2
        with app.app_context():
            with patch('app.repositories.sql_credit_card_repository.db.session.query') as query_mock:
                query_mock().filter().first.return_value = None

                credit_card = self.credit_card_repository.get_credit_card(card_id)

                self.assertIsNone(credit_card)

    def test_create_credit_card(self):
        with app.app_context():
            with patch('app.repositories.sql_credit_card_repository.db.session.commit') as commit_mock:
                credit_card_data = {
                    'exp_date': '01/23',
                    'holder': 'Luan Santos',
                    'number': '1234567812345678',
                    'cvv': '123',
                    'brand': 'Visa'
                }
                credit_card = self.credit_card_repository.create_credit_card(credit_card_data)

                self.assertEqual(credit_card.exp_date, credit_card_data['exp_date'])
                self.assertEqual(credit_card.holder, credit_card_data['holder'])
                self.assertEqual(credit_card.number, credit_card_data['number'])
                self.assertEqual(credit_card.cvv, credit_card_data['cvv'])
                self.assertEqual(credit_card.brand, credit_card_data['brand'])
                commit_mock.assert_called_once()


if __name__ == '__main__':
    unittest.main()
