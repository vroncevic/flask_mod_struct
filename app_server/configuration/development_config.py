# encoding: utf-8
__author__ = "Vladimir Roncevic"
__copyright__ = "Copyright 2017, Free software to use and distributed it."
__credits__ = ["Vladimir Roncevic"]
__license__ = "GNU General Public License (GPL)"
__version__ = "1.0.0"
__maintainer__ = "Vladimir Roncevic"
__email__ = "elektron.ronca@gmail.com"
__status__ = "Updated"

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
			DB_USER - Database connection username
			DB_PASSWORD - Database connection user password
			DB_HOST - Database server address
			DB_PORT - Database server port
			DB_DIALECT - Database dialect prefix
			SQLALCHEMY_DATABASE_URI - Set DB URI
			DEBUG_TB_ENABLED - Flask debug toolbar's
		method:
			None
	"""

	DEBUG = True
	BCRYPT_LOG_ROUNDS = 4
	WTF_CSRF_ENABLED = False
	DB_USER = "mydbuser"
	DB_PASSWORD = "mydbpassword"
	DB_HOST = "127.0.0.1"
	DB_PORT = 3306
	DB_NAME = "manage_users"
	DB_DIALECT = "mysql+mysqlconnector"
	SQLALCHEMY_DATABASE_URI = "{0}://{1}:{2}@{3}:{4}/{5}".format(
		DB_DIALECT, DB_USER, DB_PASSWORD, DB_HOST, DB_PORT, DB_NAME
	)
	DEBUG_TB_ENABLED = True