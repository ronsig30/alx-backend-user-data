#!/usr/bin/env python3

import uuid
from sqlalchemy.exc import NoResultFound
import bcrypt
from models import User
from db import DB


class Auth:
    """
    Class to handle user authentication.
    """
    def __init__(self):
        """
        Initializes the Auth instance with a database connection.
        """
        self.db = DB()

    def register_user(self, email: str, password: str) -> None:
        """
        Registers a new user with the provided email and password.

        Args:
            email (str): The email of the user.
            password (str): The password of the user.

        Raises:
            ValueError: If the email is already registered.
        """
        hashed_password = self._hash_password(password)
        try:
            self.db.add_user(email, hashed_password)
        except ValueError:
            raise ValueError("User already exists")

    def _hash_password(self, password: str) -> bytes:
        """
        Hashes the password using bcrypt.

        Args:
            password (str): The password to hash.

        Returns:
            bytes: The hashed password.
        """
        salt = bcrypt.gensalt()
        return bcrypt.hashpw(password.encode(), salt)

    def valid_login(self, email: str, password: str) -> bool:
        """
        Validates the user's login credentials.

        Args:
            email (str): The email of the user.
            password (str): The password of the user.

        Returns:
            bool: True if the login is valid, False otherwise.
        """
        try:
            user = self.db.find_user_by(email=email)
        except NoResultFound:
            return False

        hashed_password = user.hashed_password
        return bcrypt.checkpw(password.encode(), hashed_password)

    def _generate_uuid(self) -> str:
        """
        Generates a new UUID and returns its string representation.

        Returns:
            str: The string representation of the UUID.
        """
        return str(uuid.uuid4())
