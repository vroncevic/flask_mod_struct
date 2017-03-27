# encoding: utf-8
__author__ = "Vladimir Roncevic"
__copyright__ = "Copyright 2017, Free software to use and distributed it."
__credits__ = ["Vladimir Roncevic"]
__license__ = "GNU General Public License (GPL)"
__version__ = "1.0.0"
__maintainer__ = "Vladimir Roncevic"
__email__ = "elektron.ronca@gmail.com"
__status__ = "Updated"

class BaseConfig(object):
	"""
	Define class BaseConfig with attribute(s) and method(s).
	Base initial configuration setup.
	It defines:
		attribute:
			SECRET_KEY - Development key for session accessing
			DEBUG - Enable/Disable debug option
			BCRYPT_LOG_ROUNDS - for bcrypt hashing utilities
			WTF_CSRF_ENABLED - Secure forms
			DEBUG_TB_ENABLED - Flask debug toolbar's
			DEBUG_TB_INTERCEPT_REDIRECTS - Should intercept redirects?
			SQLALCHEMY_TRACK_MODIFICATIONS - Requires extra memory (True)
		method:
			None
	"""

	SECRET_KEY = "my_precious"
	DEBUG = True
	BCRYPT_LOG_ROUNDS = 4
	WTF_CSRF_ENABLED =False
	DEBUG_TB_ENABLED = True
	DEBUG_TB_INTERCEPT_REDIRECTS = False
	SQLALCHEMY_TRACK_MODIFICATIONS = False
