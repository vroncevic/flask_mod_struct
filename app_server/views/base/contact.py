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
from flask import render_template, request, flash
from flask_mail import Message

from app_server import app, mail
from app_server.forms.base.contact import ContactForm

class Contact(View):
	"""
	Define class Contact with attribute(s) and method(s).
	View for contact page.
	It defines:
		attribute:
			methods - Handler methods
		method:
			dispatch_request - Method view for contact page
	"""

	methods = ["GET", "POST"]

	def dispatch_request(self):
		"""
		:return: Value of the view or error handler
		:rtype: View
		"""
		form = ContactForm(request.form)
		if form.validate_on_submit():
			subject = request.form.get("subject")
			message = request.form.get("message")
			name = request.form.get("name")
			email = request.form.get("email")
			msg = Message(
				subject=subject,
				sender=app.config.get("MAIL_USERNAME"),
				recipients=[app.config.get("MAIL_RECIPIENT")]
			)
			msg.body = "{0}\n{1}\n{2}".format(message, name, email)
			mail.send(msg)
			flash("Message sent!", "success")
		return render_template("base/contact.html", form=form)
