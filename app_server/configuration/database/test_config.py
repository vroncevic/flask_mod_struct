# encoding: utf-8
__author__ = "Vladimir Roncevic"
__copyright__ = "Copyright 2017, Free software to use and distributed it."
__credits__ = ["Vladimir Roncevic"]
__license__ = "GNU General Public License (GPL)"
__version__ = "1.0.0"
__maintainer__ = "Vladimir Roncevic"
__email__ = "elektron.ronca@gmail.com"
__status__ = "Updated"

from app_server.configuration.database import BaseConfig

class TestConfig(BaseConfig):
	"""
	Define class TestConfig with attribute(s) and method(s).
	Testing configuration setup.
	It defines:
		attribute:
			SQLALCHEMY_DATABASE_URI - Set DB URI
		method:
			None
	"""

	SQLALCHEMY_DATABASE_URI = "sqlite:///test_phase.sqlite"
