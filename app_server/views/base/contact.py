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

class Contact(View):
	"""
	Define class Contact with attribute(s) and method(s).
	View for contact page.
	It defines:
		attribute:
			None
		method:
			dispatch_request - Method view for contact page
	"""

	def dispatch_request(self):
		"""
		:return: Value of the view or error handler
		:rtype: View
		"""
		return render_template("base/contact.html")
