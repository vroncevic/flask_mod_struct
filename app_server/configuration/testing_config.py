# encoding: utf-8
__author__ = "Vladimir Roncevic"
__copyright__ = "Copyright 2017, Free software to use and distributed it."
__credits__ = ["Vladimir Roncevic"]
__license__ = "GNU General Public License (GPL)"
__version__ = "1.0.0"
__maintainer__ = "Vladimir Roncevic"
__email__ = "elektron.ronca@gmail.com"
__status__ = "Updated"

class TestingConfig(object):
	"""
	Define class TestingConfig with attribute(s) and method(s).
	Testing configuration class.
	It defines:
		attribute:
			DEBUG - Enable/Disable debug option
			TESTING - Enable/Disable testing
			BCRYPT_LOG_ROUNDS - for bcrypt hashing utilities
			WTF_CSRF_ENABLED - Secure forms
			SQLALCHEMY_DATABASE_URI - Set DB URI
			DEBUG_TB_ENABLED - Flask debug toolbar's
			PRESERVE_CONTEXT_ON_EXCEPTION - Don't keep exception context
		method:
			None
	"""

	DEBUG = True
	TESTING = True
	BCRYPT_LOG_ROUNDS = 4
	WTF_CSRF_ENABLED = False
	SQLALCHEMY_DATABASE_URI = "sqlite:///"
	DEBUG_TB_ENABLED = False
	PRESERVE_CONTEXT_ON_EXCEPTION = False
