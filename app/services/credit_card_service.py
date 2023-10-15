from flask import jsonify

from app.repositories.credit_card_repository import CreditCardRepository
from app.validation import CreditCardValidator
from app.handlers import CreditCardHandler

credit_card_handler = CreditCardHandler()


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
        if "exp_date" in payload and "number" in payload:
            formatted_exp_date = self.validator.format_exp_date(payload["exp_date"])

            validate_card = self.validator.is_valid_card_number(payload["number"])

            if validate_card is False:
                return {"error": "Credit card is invalid"}, 422

            brand = self.validator.get_brand_by_card_number(payload["number"])

            credit_card = credit_card_handler.encrypt_credit_card_number(payload["number"])

            if formatted_exp_date:
                new_credit_card = {
                    "exp_date": formatted_exp_date,
                    "holder": payload["holder"],
                    "number": credit_card,
                    "cvv": payload["cvv"],
                    "brand": brand
                }

                created_credit_card = self.repository.create_credit_card(new_credit_card)

                if created_credit_card:
                    return created_credit_card, 201
                else:
                    return {"error": "Failed to create credit card"}, 400

            else:
                return {"error": "Invalid expiration date format"}, 400
        else:
            return {"error": "Missing required data in payload"}, 400
