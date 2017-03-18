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

class DropDatabase(Command):
	"""
	Define class DropDatabase with attribute(s) and method(s).
	Drop database with tables.
	It defines:
		attribute:
			db - SQLAlchemy integration object
		method:
			__init__ - Initial constructor
			run - Drop database
	"""

	def __init__(self, db):
		"""
		:param db: SQLAlchemy integration object
		:type: SQLAlchemy
		"""
		super(DropDatabase, self).__init__()
		self.db = db

	def run(self):
		self.db.drop_all()
