# -*- coding: utf-8 -*-

"""
 Module
     test_config.py
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
     Define class TestDevelopmentConfig, TestTestingConfig,
     TestProductionConfig with attribute(s) and method(s).
"""

__author__ = "Vladimir Roncevic"
__copyright__ = "Copyright 2017, Free software to use and distributed it."
__credits__ = ["Vladimir Roncevic"]
__license__ = "GNU General Public License (GPL)"
__version__ = "1.0.0"
__maintainer__ = "Vladimir Roncevic"
__email__ = "elektron.ronca@gmail.com"
__status__ = "Updated"

import sys
import unittest

try:
    from flask import current_app
    from flask_testing import TestCase
    from app_server import app
except ImportError as error:
    MESSAGE = "\n{0}\n{1}\n".format(__file__, error)
    sys.exit(MESSAGE)  # Force close python ATS ##############################


class TestDevelopmentConfig(TestCase):
    """
        Define class TestDevelopmentConfig with attribute(s) and method(s).
        Define TestDevelopmentConfig for testing app.
        It defines:

            :attributes:
                | None
            :methods:
                | create_app - Create app based on config
                | test_app_is_development - Checking development config
    """

    def create_app(self):
        """
            Create app based on config

            :exceptions: None
        """
        app.config.from_object("app_server.configuration.DevelopmentConfig")
        return app

    def test_app_is_development(self):
        """
            Checking development config

            :exceptions: None
        """
        self.assertFalse(current_app.config["TESTING"])
        self.assertTrue(app.config["DEBUG"] is True)
        self.assertTrue(app.config["WTF_CSRF_ENABLED"] is False)
        self.assertTrue(app.config["DEBUG_TB_ENABLED"] is True)
        self.assertFalse(current_app is None)

class TestTestingConfig(TestCase):
    """
        Define class TestTestingConfig with attribute(s) and method(s).
        Define TestTestingConfig for testing app.
        It defines:

            :attributes:
                | None
            :methods:
                | create_app - Create app based on config
                | test_app_is_testing - Checking test config
    """

    def create_app(self):
        """
            Create app based on config

            :exceptions: None
        """
        app.config.from_object("app_server.configuration.TestingConfig")
        return app

    def test_app_is_testing(self):
        """
            Checking test config

            :exceptions: None
        """
        self.assertTrue(current_app.config["TESTING"])
        self.assertTrue(app.config["DEBUG"] is True)
        self.assertTrue(app.config["BCRYPT_LOG_ROUNDS"] == 4)
        self.assertTrue(app.config["WTF_CSRF_ENABLED"] is False)

class TestProductionConfig(TestCase):
    """
        Define class TestProductionConfig with attribute(s) and method(s).
        Define TestProductionConfig for testing app.
        It defines:

            :attributes:
                | None
            :methods:
                | create_app - Create app based on config
                | test_app_is_production - Checking production config
    """

    def create_app(self):
        """
            Create app based on config

            :exceptions: None
        """
        app.config.from_object("app_server.configuration.ProductionConfig")
        return app

    def test_app_is_production(self):
        """
            Checking production config

            :exceptions: None
        """
        self.assertFalse(current_app.config["TESTING"])
        self.assertTrue(app.config["DEBUG"] is False)
        self.assertTrue(app.config["DEBUG_TB_ENABLED"] is False)
        self.assertTrue(app.config["WTF_CSRF_ENABLED"] is True)
        self.assertTrue(app.config["BCRYPT_LOG_ROUNDS"] == 13)

if __name__ == "__main__":
    unittest.main()
