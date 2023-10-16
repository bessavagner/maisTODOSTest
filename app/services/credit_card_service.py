from flask import jsonify

from app import app
from app.repositories.credit_card_repository import CreditCardRepository
from app.validation import CreditCardValidator
from app.handlers import CreditCardHandler

credit_card_handler = CreditCardHandler()


class CreditCardService:
    def __init__(self, repository: CreditCardRepository):
        self.repository = repository
        self.validator = CreditCardValidator()

    def list_credit_cards(self):
        app.logger.info('CreditCardService - listCreditCards - call repository to return all credit cards')
        credit_cards = self.repository.list_credit_cards()

        app.logger.info('CreditCardService - listCreditCards - return all credit cards')
        return credit_cards

    def get_credit_card(self, card_id):
        app.logger.info(f'CreditCardService - listCreditCard - call repository to return credit card by ID: {card_id}')
        credit_card = self.repository.get_credit_card(card_id)

        app.logger.info(f'CreditCardService - listCreditCard - return credit card by ID: {card_id}')
        return credit_card

    def create_credit_card(self, payload):
        if "exp_date" in payload and "number" in payload:
            app.logger.info('CreditCardService - createCreditCard - formate expiration date')
            formatted_exp_date = self.validator.format_exp_date(payload["exp_date"])

            app.logger.info('CreditCardService - createCreditCard - validate if card number is valid')
            validate_card = self.validator.is_valid_card_number(payload["number"])

            if validate_card is False:
                app.logger.error('CreditCardService - createCreditCard - card number is invalid')
                return {"error": "Credit card is invalid"}, 422

            app.logger.info('CreditCardService - createCreditCard - get brand by card number')
            brand = self.validator.get_brand_by_card_number(payload["number"])

            app.logger.info('CreditCardService - createCreditCard - encrypt card number')
            credit_card = credit_card_handler.encrypt_credit_card_number(payload["number"])

            if formatted_exp_date:
                app.logger.info('CreditCardService - createCreditCard - mount payload to create credit card')
                new_credit_card = {
                    "exp_date": formatted_exp_date,
                    "holder": payload["holder"],
                    "number": credit_card,
                    "cvv": payload["cvv"],
                    "brand": brand
                }

                app.logger.info('CreditCardService - createCreditCard - call credit card create in repository')
                created_credit_card = self.repository.create_credit_card(new_credit_card)

                if created_credit_card:
                    app.logger.info('CreditCardService - createCreditCard - return created credit card')
                    return created_credit_card, 201
                else:
                    app.logger.error('CreditCardService - createCreditCard - failed to create')
                    return {"error": "Failed to create credit card"}, 400

            else:
                app.logger.error('CreditCardService - createCreditCard - invalid format to expiration date')
                return {"error": "Invalid expiration date format"}, 400
        else:
            app.logger.error('CreditCardService - createCreditCard - missing args in payload')
            return {"error": "Missing required data in payload"}, 400
