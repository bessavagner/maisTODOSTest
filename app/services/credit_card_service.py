from app.repositories.credit_card_repository import CreditCardRepository

credit_card_repository = CreditCardRepository()


def list_credit_cards():
    return credit_card_repository.list_credit_cards()


class CreditCardService:
    pass
