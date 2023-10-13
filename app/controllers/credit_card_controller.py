from webargs.flaskparser import use_args
from pydantic import ValidationError
from flask import request, jsonify
from app import app
from app.args import credit_card_args
from app.models.credit_card import CreditCard
from app.services.credit_card_service import CreditCardService
from app.repositories.sql_credit_card_repository import SQLCreditCardRepository
from app.schemas.schemas import CreditCardSchema

credit_card_repository = SQLCreditCardRepository(CreditCard)
credit_card_service = CreditCardService(credit_card_repository)


@app.route('/api/v1/credit-card', methods=['GET'])
def list_credit_cards():
    credit_cards = credit_card_service.list_credit_cards()
    return jsonify([card.to_dict() for card in credit_cards])


@app.route('/api/v1/credit-card/<int:card_id>', methods=['GET'])
def get_credit_card(card_id):
    credit_card = credit_card_service.get_credit_card(card_id)

    if credit_card:
        return jsonify(credit_card, 200)
    else:
        return jsonify({"message": "Credit card not found"}, 404)


@app.route('/api/v1/credit-card', methods=['POST'])
@use_args(credit_card_args)
def create_credit_card(args):
    data = request.json

    if not data:
        return jsonify({"message": "Request body is required"}, 400)

    try:
        credit_card_data = validate_and_parse_credit_card_data(data)
    except ValidationError:
        return jsonify({"message": "Invalid request data"}, 400)

    if credit_card_service.create_credit_card(credit_card_data):
        return jsonify({"message": "Credit card created successfully"}, 201)
    else:
        return jsonify({"message": "Failed to create credit card"}, 400)


def validate_and_parse_credit_card_data(data):
    try:
        credit_card_data = CreditCardSchema(**data).dict()
        return credit_card_data
    except ValidationError as e:
        raise e
