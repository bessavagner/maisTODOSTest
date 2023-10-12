from webargs.flaskparser import use_args
from app.schemas.schemas import CreditCardSchema
from flask import Flask, request, jsonify
from app import app
from app.models.credit_card import CreditCard
from app.services.credit_card_service import CreditCardService
from app.repositories.sql_credit_card_repository import SQLCreditCardRepository
from webargs.flaskparser import use_args

credit_card_repository = SQLCreditCardRepository()
credit_card_service = CreditCardService(credit_card_repository)
credit_card_schema = CreditCardSchema()


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
@use_args(credit_card_schema)
def create_credit_card(args):
    data = request.get_json()

    if data is None:
        return jsonify({"message": "Request body is required"}, 400)

    credit_card = CreditCard(
        exp_date=args['exp_date'],
        holder=args['holder'],
        number=args['number'],
        cvv=args.get('cvv')
    )

    if credit_card_service.create_credit_card(credit_card):
        return jsonify({"message": "Credit card created successfully"}, 201)
    else:
        return jsonify({"message": "Failed to create credit card"}, 400)

