# -*- coding: utf-8 -*-

"""
 Module
     model_user.py
 Copyright
     Copyright (C) 2017 Vladimir Roncevic <elektron.ronca@gmail.com>
     flask_mod_struct is free software: you can redistribute it and/or
     modify it under the terms of the GNU General Public License as
     published by the Free Software Foundation, either version 3 of
     the License, or (at your option) any later version.
     flask_mod_struct is distributed in the hope that it will be useful,
     but WITHOUT ANY WARRANTY; without even the implied warranty of
     MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
     See the GNU General Public License for more details.
     You should have received a copy of the GNU General Public License
     along with this program. If not, see <http://www.gnu.org/licenses/>.
 Info
     Define class User with attribute(s) and method(s).
     Model for user data.
"""

import datetime
import sys

try:
    from app_server import app, db, bcrypt
    from app_server.models import Base
except ImportError as error_message:
    MESSAGE = "\n{0}\n{1}\n".format(__file__, error_message)
    sys.exit(MESSAGE)  # Force close python ATS ##############################

__author__ = "Vladimir Roncevic"
__copyright__ = "Copyright 2017, Free software to use and distributed it."
__credits__ = ["Vladimir Roncevic"]
__license__ = "GNU General Public License (GPL)"
__version__ = "1.1.0"
__maintainer__ = "Vladimir Roncevic"
__email__ = "elektron.ronca@gmail.com"
__status__ = "Updated"


class User(Base):
    """
        Define class User with attribute(s) and method(s).
        Define model user for authentication and authorization.
        It defines:

            :attributes:
                | __tablename__ - Table name
                | fullname - First and last name
                | username - User authentication name
                | password - User authentication password
                | email - User contact email
                | admin - User control flag (role)
            :methods:
                | __init__ - Initial constructor
                | get_id - Getting id
                | is_authenticated - Authentication status
                | is_active - Getting status
                | is_anonymous - Getting info
                | __repr__ - Printable representation of the User
    """

    __tablename__ = "users"

    fullname = db.Column(db.String(255), unique=True, nullable=False)
    username = db.Column(db.String(255), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)
    email = db.Column(db.String(255), unique=True, nullable=False)
    admin = db.Column(db.Boolean, nullable=False, default=False)

    def __init__(self, username, password, admin=False):
        """
            Initial constructor

            :param username: User authentication name
            :type: <str>
            :param password: User authentication password
            :type: <str>
            :param admin: Marking user as Administrator
            :type: <bool>
            :exceptions: None
        """
        self.username = username
        self.password = bcrypt.generate_password_hash(
            password, app.config.get("BCRYPT_LOG_ROUNDS")
        )
        self.modified = self.created = datetime.datetime.now()
        self.admin = admin

    def get_id(self):
        """
            Getting ID

            :return: Getting id
            :type: <int>
            :exceptions: None
        """
        return self.id

    def is_authenticated(self):
        """
            Authentication status

            :return: Authentication status
            :type: <bool>
            :exceptions: None
        """
        return True

    def is_active(self):
        """
            Get status

            :return: Getting status
            :type: <bool>
            :exceptions: None
        """
        return True

    def is_anonymous(self):
        """
            Getting info

            :return: Getting info
            :type: <bool>
            :exceptions: None
        """
        return False

    def __repr__(self):
        """
            Printable representation of the User

            :return: Printable representation of the User
            :type: <str>
            :exceptions: None
        """
        return "<{0} {1}>".format(self.__class__.__name__, self.username)
