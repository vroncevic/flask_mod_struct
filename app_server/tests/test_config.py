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
from flask import current_app
from flask_testing import TestCase
from app_server import app

class TestDevelopmentConfig(TestCase):

	def create_app(self):
		app.config.from_object("app_server.configuration.DevelopmentConfig")
		return app

	def test_app_is_development(self):
		self.assertFalse(current_app.config["TESTING"])
		self.assertTrue(app.config["DEBUG"] is True)
		self.assertTrue(app.config["WTF_CSRF_ENABLED"] is False)
		self.assertTrue(app.config["DEBUG_TB_ENABLED"] is True)
		self.assertFalse(current_app is None)

class TestTestingConfig(TestCase):

	def create_app(self):
		app.config.from_object("app_server.configuration.TestingConfig")
		return app

	def test_app_is_testing(self):
		self.assertTrue(current_app.config["TESTING"])
		self.assertTrue(app.config["DEBUG"] is True)
		self.assertTrue(app.config["BCRYPT_LOG_ROUNDS"] == 4)
		self.assertTrue(app.config["WTF_CSRF_ENABLED"] is False)

class TestProductionConfig(TestCase):

	def create_app(self):
		app.config.from_object("app_server.configuration.ProductionConfig")
		return app

	def test_app_is_production(self):
		self.assertFalse(current_app.config["TESTING"])
		self.assertTrue(app.config["DEBUG"] is False)
		self.assertTrue(app.config["DEBUG_TB_ENABLED"] is False)
		self.assertTrue(app.config["WTF_CSRF_ENABLED"] is True)
		self.assertTrue(app.config["BCRYPT_LOG_ROUNDS"] == 13)

if __name__ == "__main__":
	unittest.main()
