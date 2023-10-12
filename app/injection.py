from injector import Binder
from app.repositories.credit_card_repository import CreditCardRepository
from app.repositories.sql_credit_card_repository import SQLCreditCardRepository
from app.services.credit_card_service import CreditCardService


def configure(binder: Binder) -> Binder:
    binder.bind(CreditCardRepository, to=SQLCreditCardRepository)
    binder.bind(CreditCardService, to=CreditCardService)
