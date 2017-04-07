# encoding: utf-8
__author__ = "Vladimir Roncevic"
__copyright__ = "Copyright 2017, Free software to use and distributed it."
__credits__ = ["Vladimir Roncevic"]
__license__ = "GNU General Public License (GPL)"
__version__ = "1.0.0"
__maintainer__ = "Vladimir Roncevic"
__email__ = "elektron.ronca@gmail.com"
__status__ = "Updated"

from app_server.configuration import BaseConfig

class TestConfig(BaseConfig):
	"""
	Define class DevelopmentConfig with attribute(s) and method(s).
	Define test configuration.
	It defines:
		attribute:
			DEBUG - Enable/Disable debug option
			WTF_CSRF_ENABLED - Secure forms
			DEBUG_TB_ENABLED - Flask debug toolbar's
			DEBUG_TB_INTERCEPT_REDIRECTS - Should intercept redirects?
			BCRYPT_LOG_ROUNDS - for bcrypt hashing utilities
		method:
			None
	"""

	DEBUG = True
	WTF_CSRF_ENABLED = False
	DEBUG_TB_ENABLED = True
	DEBUG_TB_INTERCEPT_REDIRECTS = True
	BCRYPT_LOG_ROUNDS = 4