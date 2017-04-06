# encoding: utf-8
__author__ = "Vladimir Roncevic"
__copyright__ = "Copyright 2017, Free software to use and distributed it."
__credits__ = ["Vladimir Roncevic"]
__license__ = "GNU General Public License (GPL)"
__version__ = "1.0.0"
__maintainer__ = "Vladimir Roncevic"
__email__ = "elektron.ronca@gmail.com"
__status__ = "Updated"

from app_server.configuration.mail import BaseConfig

class TestConfig(BaseConfig):
	"""
	Define class DevelopmentConfig with attribute(s) and method(s).
	Define mail test email.
	It defines:
		attribute:
			MAIL_USERNAME - Mail username
			MAIL_PASSWORD - Mail password
			MAIL_RECIPIENT - Mail username
		method:
			None
	"""

	MAIL_USERNAME = ""
	MAIL_PASSWORD = ""
	MAIL_RECIPIENT = ""
