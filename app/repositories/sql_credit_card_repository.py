from app import db
from app.models.credit_card import CreditCard
from app.repositories.credit_card_repository import CreditCardRepository


class SQLCreditCardRepository(CreditCardRepository):
    def list_credit_cards(self):
        return CreditCard.query.all()

    def get_credit_card(self, id):
        return CreditCard.query.get(id)

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
