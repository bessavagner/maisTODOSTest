from webargs import fields

credit_card_args = {
    'exp_date': fields.Str(required=True),
    'holder': fields.Str(required=True),
    'number': fields.Str(required=True),
    'cvv': fields.Str(),
    'brand': fields.Str()
}