import json
from faker import Faker
import pytest
from app import app, db
from app.repositories.sql_credit_card_repository import SQLCreditCardRepository
from app.services.credit_card_service import CreditCardService
from unittest.mock import Mock

app.config['TESTING'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory/'

app_context = app.app_context()
app_context.push()

db.create_all()
client = app.test_client()

credit_card_repository = Mock(spec=SQLCreditCardRepository)
credit_card_service = CreditCardService(credit_card_repository)
fake = Faker()

@pytest.fixture
def cleanup_database():
    yield
    with app.app_context():
        db.session.remove()
        db.drop_all()


def test_register_user(cleanup_database):
    password = fake.password()
    data = {
        'email': fake.email(),
        'password': password,
        'confirm_password': password
    }
    response = client.post('/api/v1/register', data=json.dumps(data), content_type='application/json')

    assert response.status_code == 201
    assert b'User registered successfully' in response.data


def test_invalid_authentication():
    response = client.post('/api/v1/login', json={'email': 'usuario@example.com', 'password': 'senha_errada'})
    assert response.status_code == 401
    assert response.get_json() == {"message": "Invalid email or password"}


def test_login_user():
    data = {
        'email': 'test@example.com',
        'password': 'testpassword'
    }
    response = client.post('/api/v1/login', data=json.dumps(data), content_type='application/json')

    assert response.status_code == 200
    assert b'Validated successfully' in response.data
    assert b'token' in response.data


def test_short_password():
    response = client.post('/api/v1/register',
                           json={'email': 'user@example.com', 'password': '123', 'confirm_password': '123'})
    assert response.status_code == 400
    assert response.get_json() == {"message": "Password is too short"}


def test_long_email():
    long_email = 'a' * 256 + '@example.com'
    response = client.post('/api/v1/register',
                           json={'email': long_email, 'password': 'password', 'confirm_password': 'password'})
    assert response.status_code == 400
    assert response.get_json() == {"message": "Email is too long"}


def test_data_output():
    response = client.get('/api/v1/user/user@example.com')
    assert response.status_code == 200
    assert 'id' in response.get_json()
    assert 'email' in response.get_json()


def test_get_user_info():
    response = client.get('/api/v1/user/test@example.com')

    assert response.status_code == 200
    assert b'email' in response.data


def test_get_nonexistent_user():
    response = client.get('/api/v1/user/nonexistent@example.com')

    assert response.status_code == 404
    assert b'User not found' in response.data


if __name__ == '__main__':
    pytest.main()
