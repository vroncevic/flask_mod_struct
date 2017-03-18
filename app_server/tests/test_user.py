# encoding: utf-8
__author__ = "Vladimir Roncevic"
__copyright__ = "Copyright 2017, Free software to use and distributed it."
__credits__ = ["Vladimir Roncevic"]
__license__ = "GNU General Public License (GPL)"
__version__ = "1.0.0"
__maintainer__ = "Vladimir Roncevic"
__email__ = "elektron.ronca@gmail.com"
__status__ = "Updated"

import unittest

from flask_login import current_user

from app_server import bcrypt
from app_server.models.model_user import User
from app_server.tests.base import BaseTestCase

class TestUserBlueprint(BaseTestCase):

	def test_correct_login(self):
		# Ensure login behaves correctly with correct credentials.
		with self.client:
			response = self.client.post(
				"/login",
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
		# Ensure logout behaves correctly - regarding the session.
		with self.client:
			self.client.post(
				"/login",
				data=dict(email="admin@admin.com", password="admin"),
				follow_redirects=True
			)
			response = self.client.get("/logout", follow_redirects=True)
			self.assertIn(b'You were logged out. Bye!', response.data)
			self.assertFalse(current_user.is_active)

	def test_logout_route_requires_login(self):
		# Ensure logout route requres logged in user.
		response = self.client.get("/logout", follow_redirects=True)
		self.assertIn(b'Please log in to access this page', response.data)

	def test_member_route_requires_login(self):
		# Ensure member route requres logged in user.
		response = self.client.get("/members", follow_redirects=True)
		self.assertIn(b'Please log in to access this page', response.data)

	def test_get_by_id(self):
		# Ensure id is correct for the current/logged in user.
		with self.client:
			self.client.post(
				"/login",
				data=dict(email="admin@admin.com", password="admin"),
				follow_redirects=True
			)
			self.assertTrue(current_user.id == 1)

	def test_registered_on_defaults_to_datetime(self):
		# Ensure that registered_on is a datetime.
		with self.client:
			self.client.post(
				"/login",
				data=dict(email="admin@admin.com", password="admin"),
				follow_redirects=True
			)
			user = User.query.filter_by(email="admin@admin.com").first()
			#self.assertIsInstance(user.registered_on, datetime.datetime)

	def test_check_password(self):
		# Ensure given password is correct after unhashing.
		user = User.query.filter_by(email="admin@admin.com").first()
		self.assertTrue(bcrypt.check_password_hash(user.password, "admin"))
		self.assertFalse(bcrypt.check_password_hash(user.password, "foobar"))

	def test_validate_invalid_password(self):
		# Ensure user can't login when the password is incorrect.
		with self.client:
			response = self.client.post(
				"/login",
				data=dict(email="admin@admin.com", password="foo_bar"),
				follow_redirects=True
			)
		self.assertIn(b'Invalid email and/or password.', response.data)

	def test_register_route(self):
		# Ensure about route behaves correctly.
		response = self.client.get("/register", follow_redirects=True)
		self.assertIn(b'<h1>Please Register</h1>\n', response.data)

	def test_user_registration(self):
		# Ensure registration behaves correctlys.
		with self.client:
			response = self.client.post(
				"/register",
				data=dict(
					email="test@tester.com", password="testing",
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
