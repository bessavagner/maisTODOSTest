from app import db
from app.models.credit_card import CreditCard
from app.repositories.credit_card_repository import CreditCardRepository
from typing import List
from sqlalchemy.exc import SQLAlchemyError


class CreditCardRepositoryException(Exception):
    pass


class SQLCreditCardRepository(CreditCardRepository):
    def __init__(self, credit_card_model):
        self.credit_card_model = credit_card_model

    def list_credit_cards(self):
        try:
            credit_cards = db.session.query(CreditCard).all()
            return credit_cards
        except SQLAlchemyError as e:
            raise CreditCardRepositoryException("Error to list credit cards")

    def get_credit_card(self, card_id):
        try:
            credit_card = db.session.query(CreditCard).filter(CreditCard.id == card_id).first()
            if credit_card:
                return credit_card.to_dict()
            else:
                return None
        except Exception as e:
            raise CreditCardRepositoryException("Error to list credit card by ID")

    def create_credit_card(self, data):
        new_credit_card = CreditCard(
            exp_date=data['exp_date'],
            holder=data['holder'],
            number=data['number'],
            cvv=data.get('cvv'),
            brand=data.get('brand')
        )
        db.session.add(new_credit_card)
        db.session.commit()
        return new_credit_card
