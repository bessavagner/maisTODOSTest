from app.repositories.credit_card_repository import CreditCardRepository


class CreditCardService:
    def __init__(self, repository: CreditCardRepository):
        self.repository = repository

    def list_credit_cards(self):
        return self.repository.list_credit_cards()
