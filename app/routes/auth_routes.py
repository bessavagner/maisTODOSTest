# routes.py
from app import app
from app.controllers.auth_controller import register, login, get_user_by_email

app.add_url_rule('/api/v1/register', 'register', register, methods=['POST'])
app.add_url_rule('/api/v1/login', 'login', login, methods=['POST'])
app.add_url_rule('/api/v1/user/<string:username>', 'get_user_by_email', get_user_by_email, methods=['GET'])
