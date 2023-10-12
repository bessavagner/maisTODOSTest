from app.middlewares import validate_exp_date, validate_holder, validate_card_number, validate_request_body
from flask import Flask, request, jsonify
from app import app
from app.models.credit_card import CreditCard
from app.services.credit_card_service import CreditCardService
from app.repositories.sql_credit_card_repository import SQLCreditCardRepository

credit_card_repository = SQLCreditCardRepository()
credit_card_service = CreditCardService(credit_card_repository)


@app.route('/api/v1/credit-card', methods=['GET'])
def list_credit_cards():
    credit_cards = credit_card_service.list_credit_cards()
    return jsonify([card.to_dict() for card in credit_cards])


@app.route('/api/v1/credit-card/<int:card_id>', methods=['GET'])
def get_credit_card(card_id):
    credit_card = credit_card_service.get_credit_card(card_id)
    if credit_card:
        return jsonify(credit_card.to_dict())
    else:
        return jsonify({"message": "Credit card not found"}, 404)


@app.route('/api/v1/credit-card', methods=['POST'])
@validate_request_body
@validate_exp_date
@validate_holder
@validate_card_number
def create_credit_card():
    data = request.get_json()
    credit_card = CreditCard.from_dict(data)
    if credit_card_service.create_credit_card(credit_card):
        return jsonify({"message": "Credit card created successfully"}, 201)
    else:
        return jsonify({"message": "Failed to create credit card"}, 400)
