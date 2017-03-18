# encoding: utf-8
__author__ = "Vladimir Roncevic"
__copyright__ = "Copyright 2017, Free software to use and distributed it."
__credits__ = ["Vladimir Roncevic"]
__license__ = "GNU General Public License (GPL)"
__version__ = "1.0.0"
__maintainer__ = "Vladimir Roncevic"
__email__ = "elektron.ronca@gmail.com"
__status__ = "Updated"

from os.path import dirname, abspath, join

from app_server.configuration.base_config import BaseConfig

class DevelopmentConfig(BaseConfig):
	"""
	Define class DevelopmentConfig with attribute(s) and method(s).
	Development configuration class.
	It defines:
		attribute:
			BASE_DIR - Module directory
			DEBUG - Enable/Disable debug option
			BCRYPT_LOG_ROUNDS - for bcrypt hashing utilities
			WTF_CSRF_ENABLED - Secure forms
			SQLALCHEMY_DATABASE_URI - Set DB URI
			DEBUG_TB_ENABLED - Flask debug toolbar's
		method:
			None
	"""

	CURRENT_DIR = abspath(dirname(__file__))
	BASE_DIR = "{0}/../".format(CURRENT_DIR)
	DEBUG = True
	BCRYPT_LOG_ROUNDS = 4
	WTF_CSRF_ENABLED = False
	SQLALCHEMY_DATABASE_URI = "sqlite:///" + join(BASE_DIR, "dev.sqlite")
	DEBUG_TB_ENABLED = True
