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

class ProductionConfig(BaseConfig):
	"""
	Define class ProductionConfig with attribute(s) and method(s).
	Production database configuration.
	It defines:
		attribute:
			DB_USER - Database connection username
			DB_PASSWORD - Database connection user password
			DB_HOST - Database server address
			DB_PORT - Database server port
			DB_DIALECT - Database dialect prefix
			SQLALCHEMY_DATABASE_URI - Set DB URI
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
