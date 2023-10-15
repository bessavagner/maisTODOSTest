import pytest
from flask import Flask, jsonify
from app import app, db
from app.models.credit_card import CreditCard
from app.repositories.sql_credit_card_repository import SQLCreditCardRepository
from app.services.credit_card_service import CreditCardService
from unittest.mock import Mock, patch

app.config['TESTING'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory/'

app_context = app.app_context()
app_context.push()

db.create_all()
client = app.test_client()

credit_card_repository = Mock(spec=SQLCreditCardRepository)
credit_card_service = CreditCardService(credit_card_repository)


def create_credit_card(data):
    response = client.post('/api/v1/credit-card', json=data)
    return response


def test_create_credit_card_without_authorization():
    data = {
        'exp_date': '2024-12-31',
        'holder': 'Test User',
        'number': 'Valid Card Number',
        'cvv': '123',
        'brand': 'Visa'
    }

    response = create_credit_card(data)
    assert response.status_code == 401


def test_list_credit_cards():
    response = client.get('/api/v1/credit-card')
    assert response.status_code == 200


def test_get_credit_card():
    data = {
        'exp_date': '2024-12-31',
        'holder': 'Test User',
        'number': 'Valid Card Number',
        'cvv': '123',
        'brand': 'Visa'
    }

    create_credit_card(data)
    response = client.get('/api/v1/credit-card/3')
    assert response.status_code == 200


def test_get_nonexistent_credit_card():
    response = client.get('/api/v1/credit-card/999')
    assert response.status_code == 404


app_context.pop()

if __name__ == '__main__':
    pytest.main()
