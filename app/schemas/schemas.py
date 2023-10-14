from marshmallow import Schema, fields


class CreditCardSchema(Schema):
    id = fields.Int()
    exp_date = fields.String()
    holder = fields.String()
    number = fields.String()
    cvv = fields.String()
    brand = fields.String()

    def validate_and_parse_credit_card_data(self, data):
        try:
            validated_data = self.load(data)
            return validated_data
        except Exception as e:
            raise e

    class Config:
        orm_mode = True
