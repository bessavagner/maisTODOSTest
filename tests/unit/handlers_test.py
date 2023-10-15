import unittest
from cryptography.fernet import Fernet
from app.handlers import CreditCardHandler


class TestCreditCardHandler(unittest.TestCase):

    def setUp(self):
        self.credit_card_handler = CreditCardHandler()
        self.card_number = "1234567890123456"
        self.encrypted_card_number = self.credit_card_handler.encrypt_credit_card_number(self.card_number)

    def test_encrypt_credit_card_number(self):
        encrypted_card_number = self.credit_card_handler.encrypt_credit_card_number(self.card_number)
        self.assertNotEqual(encrypted_card_number,
                            self.card_number)

    def test_decrypt_valid_credit_card_number(self):
        decrypted_card_number = self.credit_card_handler.decrypt_credit_card_number(self.encrypted_card_number)
        self.assertEqual(decrypted_card_number, self.card_number)

    def test_decrypt_invalid_credit_card_number(self):
        invalid_token = b'InvalidToken'
        decrypted_card_number = self.credit_card_handler.decrypt_credit_card_number(invalid_token)
        self.assertEqual(decrypted_card_number, "Número inválido ou incorreto")


if __name__ == '__main__':
    unittest.main()
