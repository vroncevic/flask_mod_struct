# -*- coding: utf-8 -*-

"""
 Module
     __init__.py
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
     Define class BaseTestCase with attribute(s) and method(s).
     Define BaseTestCase for adding user to db.
"""

import sys

try:
    from flask_testing import TestCase
    from app_server import app, db, bcrypt
    from app_server.models.model_user import User
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


class BaseTestCase(TestCase):
    """
        Define class BaseTestCase with attribute(s) and method(s).
        Define BaseTestCase for adding user to db.
        It defines:

            :attributes:
                | None
            :methods:
                | create_app - Create app based on config
                | setUp - Setup db and user
                | tearDown - Remove session and drop db
    """

    def create_app(self):
        """
            Create app based on config

            :return: Application instance
            :rtype: <Flask>
            :exceptions: None
        """
        app.config.from_object("app_server.configuration.TestConfig")
        return app

    def setUp(self):
        """
            Setup db and user

            :exceptions: None
        """
        db.create_all()
        admin_password = bcrypt.generate_password_hash(
            "admin", app.config.get('BCRYPT_LOG_ROUNDS')
        )
        user = User(
            username=admin_password, password="admin", admin=True
        )
        user.fullname="Flask Administrator"
        user.email="admin@admin.com"
        db.session.add(user)
        db.session.commit()

    def tearDown(self):
        """
            Remove session and drop db

            :exceptions: None
        """
        db.session.remove()
        db.drop_all()
