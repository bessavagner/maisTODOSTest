from flask_injector import FlaskInjector

from app import app
from app.injection import configure

if __name__ == '__main__':
    FlaskInjector(app=app, modules=[configure])
    app.run(debug=True)
