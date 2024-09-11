#!/usr/bin/env python3
"""
User model for the users table
"""

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class User(Base):
    """
    User model for representing users in the database.
    Attributes:
        id (int): The primary key of the user.
        email (str): The user's email, non-nullable.
        hashed_password (str): The hashed password, non-nullable.
        session_id (str): Optional session ID for the user.
        reset_token (str): Optional reset token for password reset.
    """
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    email = Column(String(250), nullable=False)
    hashed_password = Column(String(250), nullable=False)
    session_id = Column(String(250), nullable=True)
    reset_token = Column(String(250), nullable=True)
