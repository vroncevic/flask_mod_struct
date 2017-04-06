# encoding: utf-8
__author__ = "Vladimir Roncevic"
__copyright__ = "Copyright 2017, Free software to use and distributed it."
__credits__ = ["Vladimir Roncevic"]
__license__ = "GNU General Public License (GPL)"
__version__ = "1.0.0"
__maintainer__ = "Vladimir Roncevic"
__email__ = "elektron.ronca@gmail.com"
__status__ = "Updated"

import datetime

from app_server import app, db, bcrypt
from app_server.models import Base

class User(Base):
	"""
	Define class User with attribute(s) and method(s).
	Model User for authentication and authorization.
	It defines:
		attribute:
			fullname - First and last name
			username - User authentication name
			password - User authentication password
			email - User contact email
			admin - User control flag (role)
		method:
			__init__ - Initial constructor
			get_id - Getting id
			is_authenticated - Authentication status
			is_active - Getting status
			is_anonymous - Getting info
			__repr__ - Printable representation of the User
	"""

	__tablename__ = "users"

	fullname = db.Column(db.String(255), unique=True, nullable=False)
	username = db.Column(db.String(255), unique=True, nullable=False)
	password = db.Column(db.String(255), nullable=False)
	email = db.Column(db.String(255), unique=True, nullable=False)
	admin = db.Column(db.Boolean, nullable=False, default=False)

	def __init__(self, username, password, admin=False):
		"""
		:param username: User authentication name
		:type: str
		:param password: User authentication password
		:type: str
		:param admin: Marking user as Administrator
		:type: bool
		"""
		self.username = username
		self.password = bcrypt.generate_password_hash(
			password, app.config.get("BCRYPT_LOG_ROUNDS")
		)
		self.modified = self.created = datetime.datetime.now()
		self.admin = admin

	def get_id(self):
		"""
		:return: Getting id
		:type: int
		"""
		return self.id

	def is_authenticated(self):
		"""
		:return: Authentication status
		:type: bool
		"""
		return True

	def is_active(self):
		"""
		:return: Getting status
		:type: bool
		"""
		return True

	def is_anonymous(self):
		"""
		:return: Getting info
		:type: bool
		"""
		return False

	def __repr__(self):
		"""
		:return: Printable representation of the User
		:type: str
		"""
		return "<{0} {1}>".format(self.__class__.__name__, self.username)
