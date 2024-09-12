#!/usr/bin/env python3
"""
Auth module
"""
from db import DB
from user import User
from bcrypt import hashpw, gensalt
from sqlalchemy.orm.exc import NoResultFound


class Auth:
    """Auth class to interact with the authentication database."""

    def __init__(self):
        self._db = DB()

    def _hash_password(self, password: str) -> bytes:
        """Hashes a password using bcrypt"""
        return hashpw(password.encode('utf-8'), gensalt())

    def register_user(self, email: str, password: str) -> User:
        """Registers a new user if the email is not already taken"""
        try:
            # Check if the user already exists
            self._db.find_user_by(email=email)
            raise ValueError(f"User {email} already exists")
        except NoResultFound:
            # If no user is found, hash the password and create a new user
            hashed_password = self._hash_password(password)
            nw_user = self._db.add_user(email, hashed_password.decode('utf-8'))
            return nw_user
