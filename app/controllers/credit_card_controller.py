from flask import Flask, request, jsonify
from app import app
from app.services.credit_card_service import CreditCardService

credit_card_service = CreditCardService()


@app.route('/api/v1/credit-card', methods=['GET'])
def list_credit_cards():
    credit_cards = credit_card_service.list_credit_cards()
    return jsonify(credit_cards)
