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
from app_server.models.model_base import Base

class User(Base):
	"""
	Define class User with attribute(s) and method(s).
	Model User for login operations.
	It defines:
		attribute:
			fullname - First and last name
			username - User short username
			password - User password
			email - User contact email
			admin - Is user Administrator
		method:
			__init__ - Initial constructor
			get_id - Getting id
			__repr__ - Printable representation of the user
	"""

	__tablename__ = "users"

	fullname = db.Column(db.String(255), unique=True, nullable=False)
	username = db.Column(db.String(255), unique=True, nullable=False)
	password = db.Column(db.String(255), nullable=False)
	email = db.Column(db.String(255), unique=True, nullable=False)
	admin = db.Column(db.Boolean, nullable=False, default=False)

	def __init__(self, fullname, username, password, email, admin=False):
		"""
		:param fullname: User fullname
		:type: str
		:param username: User system name
		:type: str
		:param password: User password
		:type: str
		:param email: User contact email
		:type: str
		:param admin: Marking user as Administrator
		:type: bool
		"""
		self.fullname = fullname
		self.username = username
		self.password = bcrypt.generate_password_hash(
			password, app.config.get("BCRYPT_LOG_ROUNDS")
		)
		self.email = email
		self.modified = self.created = datetime.datetime.now()
		self.admin = admin

	def get_id(self):
		"""
		:return: Getting id
		:type: int
		"""
		return self.id

	def __repr__(self):
		"""
		:return: Printable representation of the user
		:type: str
		"""
		return "<{0} {1} {2} {3} {4}>".format(
			self.__class__.__name__, self.fullname, self.username,
			self.email, self.admin
		)
