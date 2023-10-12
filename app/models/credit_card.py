from app import db


class CreditCard(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    exp_date = db.Column(db.String(7), nullable=False)
    holder = db.Column(db.String(255), nullable=False)
    number = db.Column(db.String(255), nullable=False, unique=True)
    cvv = db.Column(db.String(4))
    brand = db.Column(db.String(255))
