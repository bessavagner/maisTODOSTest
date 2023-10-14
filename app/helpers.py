from functools import wraps
from flask import request, jsonify
import jwt
from app.controllers.auth_controller import get_user_by_email

from app import app


def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        auth_header = request.headers.get('Authorization')
        if not auth_header:
            return jsonify({'message': 'Token is missing from the Authorization header', 'data': []}), 401

        parts = auth_header.split()
        if len(parts) != 2 or parts[0].lower() != 'bearer':
            return jsonify({'message': 'Invalid token format', 'data': []}), 401

        token = parts[1]

        try:
            data = jwt.decode(token, app.config['SECRET_KEY'], algorithms=['HS256'])
            current_user = get_user_by_email(username=data['username'])
        except jwt.ExpiredSignatureError:
            return jsonify({'message': 'Token has expired', 'data': []}), 401
        except jwt.InvalidTokenError:
            return jsonify({'message': 'Token is invalid', 'data': []}), 401

        return f(current_user, *args, **kwargs)

    return decorated
