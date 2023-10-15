from sqlalchemy import Column, Integer, String, Date
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class CreditCard(Base):
    __tablename__ = 'credit_cards'

    id = Column(Integer, primary_key=True)
    exp_date = Column(Date)
    holder = Column(String)
    number = Column(String)
    cvv = Column(String)
    brand = Column(String)

    def to_dict(self):
        return {
            'id': self.id,
            'exp_date': self.exp_date,
            'holder': self.holder,
            'number': self.number,
            'cvv': self.cvv,
            'brand': self.brand
        }
