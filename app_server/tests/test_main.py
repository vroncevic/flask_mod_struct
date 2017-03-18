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
from app_server.tests.base import BaseTestCase

class TestMainBlueprint(BaseTestCase):

	def test_index(self):
		# Ensure Flask is setup.
		response = self.client.get("/", follow_redirects=True)
		self.assertEqual(response.status_code, 200)
		self.assertIn(b'Welcome!', response.data)
		self.assertIn(b'Register/Login', response.data)

	def test_about(self):
		# Ensure about route behaves correctly.
		response = self.client.get("/about", follow_redirects=True)
		self.assertEqual(response.status_code, 200)
		self.assertIn(b'About', response.data)

	def test_404(self):
		# Ensure 404 error is handled.
		response = self.client.get("/404")
		self.assert404(response)
		self.assertTemplateUsed("errors/404.html")

if __name__ == "__main__":
	unittest.main()
