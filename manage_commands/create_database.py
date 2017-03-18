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

class CreateDatabase(Command):
	"""
	Define class CreateDatabase with attribute(s) and method(s).
	Create database with tables defined by models.
	It defines:
		attribute:
			db - SQLAlchemy integration object
		method:
			__init__ - Initial constructor
			run - Create database with tables.
	"""

	def __init__(self, db):
		"""
		:param db: SQLAlchemy integration object
		:type: SQLAlchemy
		"""
		super(CreateDatabase, self).__init__()
		self.db = db

	def run(self):
		self.db.create_all()
