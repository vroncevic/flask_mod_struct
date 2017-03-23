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
from flask import redirect, session, flash, url_for
from flask_login import logout_user, login_required

class Logout(View):
	"""
	Define class Logout with attribute(s) and method(s).
	Logout view.
	It defines:
		attribute:
			decorators - List of decorators
		method:
			dispatch_request - Method view for logout operation
	"""

	decorators = [login_required]

	def dispatch_request(self):
		"""
		:return: Value of the view or error handler
		:rtype: View
		"""
		logout_user()
		session["logged_in"] = False
		flash("You were logged out. Bye!", "success")
		return redirect(url_for("base.home"))
