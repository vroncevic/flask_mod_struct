# encoding: utf-8
__author__ = "Vladimir Roncevic"
__copyright__ = "Copyright 2017, Free software to use and distributed it."
__credits__ = ["Vladimir Roncevic"]
__license__ = "GNU General Public License (GPL)"
__version__ = "1.0.0"
__maintainer__ = "Vladimir Roncevic"
__email__ = "elektron.ronca@gmail.com"
__status__ = "Updated"

import sys
from getpass import getpass

from flask_script import Command

from app_server.models.model_user import User

class CreateSuperUser(Command):
	"""
	Define class CreateSuperUser with attribute(s) and method(s).
	Create superuser and insert to database.
	It defines:
		attribute:
			__db - SQLAlchemy integration object
		method:
			__init__ - Initial constructor
			run - Create superuser and insert to database
	"""

	def __init__(self, db):
		"""
		:param db: SQLAlchemy integration object
		:type: SQLAlchemy
		"""
		super(CreateSuperUser, self).__init__()
		self.__db = db

	def run(self):
		print("Create superuser account")
		if sys.version_info < (3, 0, 0):
			# noinspection PyCompatibility
			username = raw_input("Insert superuser username: ")
			# noinspection PyCompatibility
			superuser_email = raw_input("Insert superuser email: ")
		elif sys.version_info >= (3, 0, 0):
			username = input("Insert superuser username: ")
			superuser_email = input("Insert superuser email: ")
		else:
			username = "admin"
			superuser_email = "admin@admin.com"
		superuser_password = getpass("Insert superuser password: ")
		admin = User(
			username=username, password=superuser_password, admin=True
		)
		admin.fullname="Flask Superuser"
		admin.email=superuser_email
		self.__db.session.add(admin)
		self.__db.session.commit()
		print("Done")
