# encoding: utf-8
__author__ = "Vladimir Roncevic"
__copyright__ = "Copyright 2017, Free software to use and distributed it."
__credits__ = ["Vladimir Roncevic"]
__license__ = "GNU General Public License (GPL)"
__version__ = "1.0.0"
__maintainer__ = "Vladimir Roncevic"
__email__ = "elektron.ronca@gmail.com"
__status__ = "Updated"

from app_server.tests.base_query import SQLAlchemyBaseQuery
from app_server.models.model_user import User

class SQLAlchemyQuery(object):
	"""
	Define class SQLAlchemyQuery with attribute(s) and method(s).
	Create session and do query.
	It defines:
		attribute:
			__session - Session maker
		method:
			__init__ - Initial constructor
	"""

	def __init__(self):
		self.__session = SQLAlchemyBaseQuery.Session()

	def query_all(self):
		for user in self.__session.query(User).all():
			print(user.fullname, user.username, user.email, user.admin)
