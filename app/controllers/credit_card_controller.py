from flask import Flask, request, jsonify
from app import app
from app.services.credit_card_service import CreditCardService
from app.repositories.sql_credit_card_repository import SQLCreditCardRepository

credit_card_repository = SQLCreditCardRepository()
credit_card_service = CreditCardService(credit_card_repository)


@app.route('/api/v1/credit-card', methods=['GET'])
def list_credit_cards():
    credit_cards = credit_card_service.list_credit_cards()
    return jsonify(credit_cards)
