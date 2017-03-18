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
from wtforms import StringField, PasswordField
from wtforms.validators import DataRequired, Email

class UserLogin(FlaskForm):
	"""
	Define class AdminLogin with attribute(s) and method(s).
	User login form (email and password).
	It defines:
		attribute:
			email - User email
			password - User password
		method:
			None
	"""

	email = StringField('Email Address', [DataRequired(), Email()])
	password = PasswordField('Password', [DataRequired()])
