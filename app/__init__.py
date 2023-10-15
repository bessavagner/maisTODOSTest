from flask import Flask, send_from_directory
from flask_migrate import Migrate
from app.config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_swagger_ui import get_swaggerui_blueprint
from flask_cors import CORS

app = Flask(__name__)
app.config.from_object(Config)
CORS(app)

SWAGGER_URL = '/api/docs'
API_URL = 'http://127.0.0.1:5000/docs/swagger.json'

swaggerui_blueprint = get_swaggerui_blueprint(
    SWAGGER_URL,
    API_URL,
    config={
        'app_name': "todos LTDA Api"
    }
)


@app.route('/docs/swagger.json')
def send_swagger():
    return send_from_directory('../docs', 'swagger.json')


app.register_blueprint(swaggerui_blueprint)

db = SQLAlchemy(app)
migrate = Migrate(app, db)

from app.controllers import credit_card_controller
from app.controllers import auth_controller
from app.routes import auth_routes
