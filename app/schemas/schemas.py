from marshmallow import Schema, fields


class CreditCardSchema(Schema):
    exp_date = fields.Str(required=True)
    holder = fields.Str(required=True)
    number = fields.Str(required=True)
    cvv = fields.Str(validate=lambda s: 3 <= len(s) <= 4)
