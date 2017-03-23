# encoding: utf-8
__author__ = "Vladimir Roncevic"
__copyright__ = "Copyright 2017, Free software to use and distributed it."
__credits__ = ["Vladimir Roncevic"]
__license__ = "GNU General Public License (GPL)"
__version__ = "1.0.0"
__maintainer__ = "Vladimir Roncevic"
__email__ = "elektron.ronca@gmail.com"
__status__ = "Updated"

from flask.views import View
from flask import render_template
from flask_login import login_required

from app_server import db
from app_server.models.model_user import User

class Administration(View):
	"""
	Define class Administration with attribute(s) and method(s).
	Administration view (list of all users).
	It defines:
		attribute:
			decorators - List of decorators
		method:
			dispatch_request - Initial constructor
	"""

	decorators = [login_required]

	def dispatch_request(self):
		"""
		:return: Value of the view or error handler
		:rtype:
		"""
		table_data = db.session.query(User).all()
		return render_template("user/administration.html", table=table_data)
