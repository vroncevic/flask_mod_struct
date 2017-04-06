# encoding: utf-8
__author__ = "Vladimir Roncevic"
__copyright__ = "Copyright 2017, Free software to use and distributed it."
__credits__ = ["Vladimir Roncevic"]
__license__ = "GNU General Public License (GPL)"
__version__ = "1.0.0"
__maintainer__ = "Vladimir Roncevic"
__email__ = "elektron.ronca@gmail.com"
__status__ = "Updated"

from flask_wtf import FlaskForm
from wtforms.fields import StringField
from wtforms.validators import DataRequired, Email
from wtforms.widgets import TextArea

class ContactForm(FlaskForm):
	"""
	Define class ContactForm with attribute(s) and method(s).
	Define contact form (sending an email).
	It defines:
		attribute:
			name - Contact name
			email - Contact email
			subject - Message subject
			message - Message body
		method:
			None
	"""

	name = StringField(
		"Name", validators=[DataRequired("Please enter your name!")]
	)
	email = StringField(
		"Email", validators=[
			DataRequired("Please enter your email address!"),
			Email("Please enter your email address!")
		]
	)
	subject = StringField(
		"Subject", validators=[DataRequired("Please enter a subject!")]
	)
	message = StringField(
		"Message", widget=TextArea(),
		validators=[DataRequired("Please enter a message!")]
	)
