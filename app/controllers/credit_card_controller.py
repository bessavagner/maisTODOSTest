import json
from pydantic import ValidationError
from flask import request, jsonify
from app import app
from app.helpers import token_required
from app.models.credit_card import CreditCard
from app.services.credit_card_service import CreditCardService
from app.repositories.sql_credit_card_repository import SQLCreditCardRepository
from app.schemas.schemas import CreditCardSchema

credit_card_repository = SQLCreditCardRepository(CreditCard)
credit_card_service = CreditCardService(credit_card_repository)


@app.route('/api/v1/credit-card', methods=['GET'])
def list_credit_cards():
    """
    List all credit cards.

    ---
    tags:
      - Credit Cards
    security:
      - Bearer Auth: []
    responses:
      200:
        description: List of credit cards.
      401:
        description: Unauthorized.
    """
    app.logger.info('CreditCardController - listCreditCards - list credit cards')
    credit_cards = credit_card_service.list_credit_cards()

    if credit_cards is not None:
        return jsonify([card.to_dict() for card in credit_cards]), 200
    else:
        app.logger.error('CreditCardController - listCreditCards - error listing credit cards')
        return jsonify({"message": "Failed to list credit cards"}), 500


@app.route('/api/v1/credit-card/<int:card_id>', methods=['GET'])
def get_credit_card(card_id):
    """
    Get a credit card by ID.

    ---
    tags:
      - Credit Cards
    security:
      - Bearer Auth: []
    parameters:
      - name: card_id
        in: path
        required: true
        type: integer
        description: ID of the credit card to retrieve.
    responses:
      200:
        description: Credit card details.
      401:
        description: Unauthorized.
      404:
        description: Credit card not found.
    """

    app.logger.info(f'CreditCardController - listOneCreditCard - list credit card by id: {card_id}')
    credit_card = credit_card_service.get_credit_card(card_id)

    if credit_card:
        app.logger.info('CreditCardController - listOneCreditCard - return founded credit card')
        return jsonify(credit_card), 200
    else:
        app.logger.error('CreditCardController - listOneCreditCard - credit card not found')
        return jsonify({"message": "Credit card not found"}), 404


@app.route('/api/v1/credit-card', methods=['POST'])
@token_required
def create_credit_card(current_user):
    """
    Create a new credit card.

    ---
    tags:
      - Credit Cards
    security:
      - Bearer Auth: []
    parameters:
      - name: credit_card_data
        in: body
        required: true
        schema:
          $ref: '#/definitions/CreditCard'
    responses:
      201:
        description: Credit card created successfully.
      400:
        description: Invalid request data.
      401:
        description: Unauthorized.
      500:
        description: Failed to create credit card.
    """
    credit_card_data = request.get_json()

    if not current_user:
        return jsonify({"message": "Unauthorized"}), 401

    if "exp_date" not in credit_card_data:
        return jsonify({"message": "Expiration date is required"}), 400

    try:
        credit_card_dict = validate_and_parse_credit_card_data(credit_card_data)
        if not credit_card_dict:
            return jsonify({"message": "Invalid credit card data"}), 400
    except Exception as e:
        app.logger.error(f'CreditCardController - createNewCreditCard - error: {str(e)}')
        return jsonify({"message": "Failed to create credit card"}), 500

    if credit_card_service.create_credit_card(credit_card_dict):
        return jsonify({"message": "Credit card created successfully"}), 201
    else:
        app.logger.error('CreditCardController - createNewCreditCard - error to create credit card')
        return jsonify({"message": "Failed to create credit card"}), 500


def validate_and_parse_credit_card_data(data):
    try:
        app.logger.info('CreditCardController - createNewCreditCard - validate and parse credit card data')
        credit_card_schema = CreditCardSchema()
        validated_data = credit_card_schema.validate_and_parse_credit_card_data(data)

        app.logger.info('CreditCardController - createNewCreditCard - return parsed data')
        parsed_data = validated_data

        return parsed_data
    except ValidationError as e:
        raise e
