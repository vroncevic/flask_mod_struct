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

class ProductionConfig(BaseConfig):
	"""
	Define class ProductionConfig with attribute(s) and method(s).
	Production configuration class.
	It defines:
		attribute:
			SECRET_KEY - Production key for session accessing
			DEBUG - Enable/Disable debug option
			SQLALCHEMY_DATABASE_URI - Set DB URI
			DEBUG_TB_ENABLED - Flask debug toolbar's
		method:
			None
	"""

	DB_USER = "mydbuser"
	DB_PASSWORD = "mydbpassword"
	DB_HOST = "127.0.0.1"
	DB_PORT = 5432
	DB_NAME = "manage_users"
	DB_DIALECT = "postgresql"
	SQLALCHEMY_DATABASE_URI = "{0}://{1}:{2}@{3}:{4}/{5}".format(
		DB_DIALECT, DB_USER, DB_PASSWORD, DB_HOST, DB_PORT, DB_NAME
	)
