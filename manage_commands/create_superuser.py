# encoding: utf-8
__author__ = "Vladimir Roncevic"
__copyright__ = "Copyright 2017, Free software to use and distributed it."
__credits__ = ["Vladimir Roncevic"]
__license__ = "GNU General Public License (GPL)"
__version__ = "1.0.0"
__maintainer__ = "Vladimir Roncevic"
__email__ = "elektron.ronca@gmail.com"
__status__ = "Updated"

from flask_script import Command
from getpass import getpass
from app_server.models.model_user import User

class CreateSuperUser(Command):
	"""
	Define class CreateSuperUser with attribute(s) and method(s).
	Create superuser and insert to database.
	It defines:
		attribute:
			db - SQLAlchemy integration object
		method:
			__init__ - Initial constructor
			run - Create admin user and add to database
	"""

	def __init__(self, db):
		"""
		:param db: SQLAlchemy integration object
		:type: SQLAlchemy
		"""
		super(CreateSuperUser, self).__init__()
		self.db = db

	def run(self):
		username = input("Insert username: ")
		superuser_email = input("Insert admin email: ")
		superuser_password = getpass("Insert admin password: ")
		self.db.session.add(
			User(
				fullname="Flask Superuser", username=username,
				password=superuser_password, email=superuser_email, admin=True
			)
		)
		self.db.session.commit()
