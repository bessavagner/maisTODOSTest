from abc import ABC, abstractmethod
from app.models.credit_card import CreditCard


class CreditCardRepository(ABC):
    @abstractmethod
    def list_credit_cards(self):
        pass

    @abstractmethod
    def get_credit_card(self, id):
        pass

    @abstractmethod
    def create_credit_card(self, data):
        pass
