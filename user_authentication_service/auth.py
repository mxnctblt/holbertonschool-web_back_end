#!/usr/bin/env python3
""" auth module """

import bcrypt
from db import DB
from user import User
from sqlalchemy.orm.exc import NoResultFound


def _hash_password(password: str) -> bytes:
    """ hash the input password """
    return bcrypt.hashpw(password.encode(), bcrypt.gensalt())


class Auth:
    """ Auth class to interact with the authentication database.
    """

    def __init__(self):
        self._db = DB()

    def register_user(self, email: str, password: str) -> User:
        """ register a user """
        if email and password:
            try:
                self._db.find_user_by(email=email)
            except NoResultFound:
                user = self._db.add_user(email, _hash_password(password))
                return user
            else:
                raise ValueError("User {} already exists".format(email))

    def valid_login(self, email: str, password: str) -> bool:
        """ check password """
        if email and password:
            try:
                user = self._db.find_user_by(email=email)
                if user:
                    return bcrypt.checkpw(password.encode(), user.hashed_password)
            except NoResultFound:
                return False
