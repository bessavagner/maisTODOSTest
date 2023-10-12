from app.repositories.credit_card_repository import CreditCardRepository
from app.validation import CreditCardValidator


class CreditCardService:
    def __init__(self, repository: CreditCardRepository):
        self.repository = repository
        self.validator = CreditCardValidator()

    def list_credit_cards(self):
        credit_cards = self.repository.list_credit_cards()
        return credit_cards

    def get_credit_card(self, key):
        credit_card = self.repository.get_credit_card(key)
        return credit_card

    def create_credit_card(self, payload):
        print("payload: ", payload)
        formatted_exp_date = self.validator.format_exp_date(payload.exp_date)

        if formatted_exp_date:
            new_credit_card = {
                "exp_date": formatted_exp_date,
                "holder": payload.holder,
                "number": payload.number,
                "cvv": payload.cvv,
                "brand": "AQUI_VAI_A_BANDEIRA",
            }

            created_credit_card = self.repository.create_credit_card(new_credit_card)

            return created_credit_card, 201
        else:
            return {"error": "Invalid expiration date format"}, 400
