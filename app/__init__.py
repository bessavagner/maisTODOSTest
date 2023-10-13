from flask import Flask
from flask_migrate import Migrate
from app.config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager
from flask_bcrypt import Bcrypt

app = Flask(__name__)
app.config.from_object(Config)

db = SQLAlchemy(app)
migrate = Migrate(app, db)

jwt = JWTManager(app)
bcrypt = Bcrypt(app)

from app.controllers import credit_card_controller
from app.controllers import auth_controller
