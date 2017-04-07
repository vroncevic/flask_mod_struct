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

from app_server.tests.sqlalchemy_query import SQLAlchemyQuery

class ORMTest(Command):
	"""
	Define class ORMTest with attribute(s) and method(s).
	Command for ORM tests.
	It defines:
		attribute:
			__query - Run query tests
		method:
			__init__ - Initial constructor
			run - Run queries.
	"""

	def __init__(self):
		super(ORMTest, self).__init__()
		self.__query = SQLAlchemyQuery()

	def run(self):
		print("Run ORM tests")
		self.__query.query_all()
		print("Done")
		return 0
