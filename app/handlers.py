from cryptography.fernet import Fernet
from cryptography.fernet import InvalidToken


class CreditCardHandler:
    def __init__(self):
        self.key = Fernet.generate_key()
        self.fernet = Fernet(self.key)

    def encrypt_credit_card_number(self, card_number):
        encrypted_card_number = self.fernet.encrypt(card_number.encode())
        return encrypted_card_number

    def decrypt_credit_card_number(self, encrypted_card_number):
        try:
            decrypted_card_number = self.fernet.decrypt(encrypted_card_number).decode()
            return decrypted_card_number
        except InvalidToken:
            return "Número inválido ou incorreto"
