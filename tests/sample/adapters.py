"""Module to hold adapter classes"""


import requests


class CreditCardsHandlerAPI:
    """
    Class for interacting with a Credit Card Handler API.

    Attributes:
        base_url (str): The base URL of the API.
        headers (dict): Default headers for API requests.

    Methods:
        __init__(): Initialize the CreditCardsHandlerAPI class.
        _start_session(): Start a new session with default headers.
        create_user(email, password, confirm_password): Create a
            new user.
        user(email): Get user information by email.
        login(user, password): Log in a user.
        create_card(number, exp_date, cvv, holder, auth): Create a
            new credit card.
        credit_cards(): Get a list of credit cards.
        credit_card(id_): Get credit card information by ID.
        update_credit_card(id_, number, exp_date, cvv, holder, auth):
            Update credit card information.
        delete_credit_card(id_, auth): Delete a credit card by ID.
    """
    base_url = 'http://127.0.0.1:5000/api/v1'
    headers = {
        "accept": "application/json",
        "Content-Type": "application/json"
    }
    def __init__(self,):
        self.cards = {}
        self.users = {}
        self.session = self._start_session()
        self.session.headers = self.headers
    
    def _start_session(self,):
        """
        Start a new session with default headers.

        Returns:
            requests.Session: A new session with default headers.
        """
        session = requests.Session()
        session.headers = self.headers
        return session
    
    def create_user(self,
                    email: str,
                    password: str,
                    confirm_password: str):
        """
        Create a new user.

        Args:
            email (str): User's email address.
            password (str): User's password.
            confirm_password (str): Confirm user's password.

        Returns:
            requests.Response: The API response after creating
            the user.
        """
        user_data = {
            "email": email,
            "password": password,
            "confirm_password": confirm_password
        }
        url = f"{self.base_url}/register"
        self.users[email] = user_data
        return self.session.post(url, json=user_data)
    
    def user(self,
             email: str):
        """
        Get user information by email.

        Args:
            email (str): User's email address.

        Returns:
            requests.Response: The API response containing user
            information.
        """
        url = f"{self.base_url}/{email}"
        return self.session.get(url)
    
    def login(self,
              user: str,
              password: str):
        """
        Log in a user.

        Args:
            user (str): User's email or username.
            password (str): User's password.

        Returns:
            requests.Response: The API response after logging in the
            user.
        """
        user_data = {
            "email": user,
            "password": password,
        }
        url = f"{self.base_url}/login"
        return self.session.post(url, json=user_data)

    def create_card(self,
                    number: str,
                    exp_date: str,
                    cvv: str,
                    holder: str,
                    auth: str):
        """
        Create a new credit card.

        Args:
            number (str): Credit card number.
            exp_date (str): Expiration date of the credit card.
            cvv (str): CVV code of the credit card.
            holder (str): Cardholder's name.
            auth (str): Authorization token.

        Returns:
            requests.Response: The API response after creating the
            credit card.
        """
        credit_card_data = {
            "number": number,
            "exp_date": exp_date,
            "cvv": cvv,
            "holder": holder
        }
        self.session.headers['Authorization'] = f"Bearer {auth}"
        url = f"{self.base_url}/credit-card"
        self.cards[number] = credit_card_data
        response = self.session.post(url, json=credit_card_data)
        return response

    def credit_cards(self,):
        """
        Get a list of credit cards.

        Returns:
            requests.Response: The API response containing a list
            of credit cards.
        """
        url = f"{self.base_url}/credit-card"
        return self.session.get(url)

    def credit_card(self, id_: int):
        """
        Get credit card information by ID.

        Args:
            id_ (int): ID of the credit card.

        Returns:
            requests.Response: The API response containing credit
            card information.
        """
        url = f"{self.base_url}/credit-card/{id_}"
        return self.session.get(url)

    def update_credit_card(self,
                           id_: int,
                           number: str,
                           exp_date: str,
                           cvv: str,
                           holder: str,
                           auth: str):
        """
        Update credit card information.

        Args:
            id_ (int): ID of the credit card to be updated.
            number (str): Updated credit card number.
            exp_date (str): Updated expiration date.
            cvv (str): Updated CVV code.
            holder (str): Updated cardholder's name.
            auth (str): Authorization token.

        Returns:
            requests.Response: The API response after updating the
            credit card information.
        """
        credit_card_data = {
            "number": number,
            "exp_date": exp_date,
            "cvv": cvv,
            "holder": holder
        }
        
        url = f"{self.base_url}/credit-card/{id_}"
        self.session.headers['Authorization'] = f"Bearer {auth}"
        self.cards[number] = credit_card_data
        response = self.session.put(url, json=credit_card_data)
        return response

    def delete_credit_card(self, id_: int, auth: str):
        """
        Delete a credit card by ID.

        Args:
            id_ (int): ID of the credit card to be deleted.
            auth (str): Authorization token.

        Returns:
            requests.Response: The API response after deleting the
            credit card.
        """
        url = f"{self.base_url}/credit-card/{id_}"
        self.session.headers['Authorization'] = f"Bearer {auth}"
        return self.session.delete(url)
