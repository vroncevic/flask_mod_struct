# -*- coding: utf-8 -*-

"""
 Module
     test_user.py
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
     Define class TestUserBlueprint with attribute(s) and method(s).
     Define TestUserBlueprint for testing App.
"""

import sys
import unittest
from datetime import datetime

try:
    from flask_login import current_user
    from app_server import bcrypt
    from app_server.forms.user.login import UserLoginForm
    from app_server.models.model_user import User
    from app_server.tests import BaseTestCase
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


class TestUserBlueprint(BaseTestCase):
    """
        Define class TestUserBlueprint with attribute(s) and method(s).
        Define TestUserBlueprint for testing App.
        It defines:

            :attributes:
                | client - Client
            :methods:
                | test_correct_login - Test correct login
                | test_logout_behaves_correctly - Test logout
                | test_logout_route_requires_login - Test logout
                | test_member_route_requires_login - Test member login
                | test_validate_success_login_form - Test login
                | test_validate_invalid_email_format - Test email
                | test_get_by_id - Get id
                | test_registered_on_defaults_to_datetime - Test register
                | test_check_password - Test password
                | test_validate_invalid_password - Test password
                | test_register_route - Test register
                | test_user_registration - Test register
    """

    def test_correct_login(self):
        """
            Test correct login

            :exceptions: None
        """
        # Ensure login behaves correctly with correct credentials.
        with self.client:
            response = self.client.post(
                "/login/",
                data=dict(email="admin@admin.com", password="admin"),
                follow_redirects=True
            )
            self.assertIn(b'Welcome', response.data)
            self.assertIn(b'Logout', response.data)
            self.assertIn(b'Members', response.data)
            self.assertTrue(current_user.email == "admin@admin.com")
            self.assertTrue(current_user.is_active())
            self.assertEqual(response.status_code, 200)

    def test_logout_behaves_correctly(self):
        """
            Test logout

            :exceptions: None
        """
        # Ensure logout behaves correctly - regarding the session.
        with self.client:
            self.client.post(
                "/login/",
                data=dict(email="admin@admin.com", password="admin"),
                follow_redirects=True
            )
            response = self.client.get("/logout/", follow_redirects=True)
            self.assertIn(b'You were logged out. Bye!', response.data)
            self.assertFalse(current_user.is_active)

    def test_logout_route_requires_login(self):
        """
            Test logout

            :exceptions: None
        """
        # Ensure logout route requres logged in user.
        response = self.client.get("/logout/", follow_redirects=True)
        self.assertIn(b'Please log in to access this page', response.data)

    def test_member_route_requires_login(self):
        """
            Test member login

            :exceptions: None
        """
        # Ensure member route requres logged in user.
        response = self.client.get("/members/", follow_redirects=True)
        self.assertIn(b'Please log in to access this page', response.data)

    def test_validate_success_login_form(self):
        """
            Test login

            :exceptions: None
        """
        # Ensure correct data validates.
        form = UserLoginForm(email="admin@admin.com", password="admin")
        self.assertTrue(form.validate_on_submit())

    def test_validate_invalid_email_format(self):
        """
            Test email

            :exceptions: None
        """
        # Ensure invalid email format throws error.
        form = UserLoginForm(email="unknown", password="example")
        self.assertFalse(form.validate_on_submit())

    def test_get_by_id(self):
        """
            Get id

            :exceptions: None
        """
        # Ensure id is correct for the current/logged in user.
        with self.client:
            self.client.post(
                "/login/",
                data=dict(email="admin@admin.com", password="admin"),
                follow_redirects=True
            )
            self.assertTrue(current_user.id == 1)

    def test_registered_on_defaults_to_datetime(self):
        """
            Test register

            :exceptions: None
        """
        # Ensure that registered_on is a datetime.
        with self.client:
            self.client.post(
                "/login/",
                data=dict(email="ad@min.com", password="admin"),
                follow_redirects=True
            )
            user = User.query.filter_by(email="admin@admin.com").first()
            # noinspection PyCompatibility
            self.assertIsInstance(user.created, datetime.datetime)

    def test_check_password(self):
        """
            Test password

            :exceptions: None
        """
        # Ensure given password is correct after unhashing.
        user = User.query.filter_by(email="admin@admin.com").first()
        self.assertTrue(bcrypt.check_password_hash(user.password, "admin"))
        self.assertFalse(bcrypt.check_password_hash(user.password, "foobar"))

    def test_validate_invalid_password(self):
        """
            Test password

            :exceptions: None
        """
        # Ensure user can't login when the password is incorrect.
        with self.client:
            response = self.client.post(
                "/login/",
                data=dict(email="admin@admin.com", password="foo_bar"),
                follow_redirects=True
            )
        self.assertIn(b'Invalid email and/or password.', response.data)

    def test_register_route(self):
        """
            Test register

            :exceptions: None
        """
        # Ensure about route behaves correctly.
        response = self.client.get("/register/", follow_redirects=True)
        self.assertIn(b'<h1>Please Register</h1>\n', response.data)

    def test_user_registration(self):
        """
            Test register

            :exceptions: None
        """
        # Ensure registration behaves correctlys.
        with self.client:
            response = self.client.post(
                "/register/",
                data=dict(
                    email="test@tester.com",
                    password="testing",
                    confirm="testing"
                ),
                follow_redirects=True
            )
            self.assertIn(b'Welcome', response.data)
            self.assertTrue(current_user.email == "test@tester.com")
            self.assertTrue(current_user.is_active())
            self.assertEqual(response.status_code, 200)

if __name__ == "__main__":
    unittest.main()
