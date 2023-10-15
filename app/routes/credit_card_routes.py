from app import app
from app.controllers.credit_card_controller import list_credit_cards, get_credit_card, create_credit_card

app.add_url_rule('/api/v1/credit-card', 'list_credit_cards', list_credit_cards, methods=['GET'])
app.add_url_rule('/api/v1/credit-card/<int:card_id>', 'get_credit_card', get_credit_card, methods=['GET'])
app.add_url_rule('/api/v1/credit-card', 'create_credit_card', create_credit_card, methods=['POST'])
