# encoding: utf-8
__author__ = "Vladimir Roncevic"
__copyright__ = "Copyright 2017, Free software to use and distributed it."
__credits__ = ["Vladimir Roncevic"]
__license__ = "GNU General Public License (GPL)"
__version__ = "1.0.0"
__maintainer__ = "Vladimir Roncevic"
__email__ = "elektron.ronca@gmail.com"
__status__ = "Updated"

from app_server import db

class Base(db.Model):
	"""
	Define class Base with attribute(s) and method(s).
	Abstract base data model.
	It defines:
		attribute:
			id - Abstract Table id
			created - Date of creation
			modified - Date of modification
		method:
			None
	"""

	__abstract__ = True

	id = db.Column(db.Integer, primary_key=True, autoincrement=True)
	created = db.Column(db.DateTime, nullable=False)
	modified = db.Column(db.DateTime, nullable=False)
