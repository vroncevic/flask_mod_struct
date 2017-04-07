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
from wtforms.validators import DataRequired, Email, Length, EqualTo

class UserRegisterForm(FlaskForm):
	"""
	Define class UserRegisterForm with attribute(s) and method(s).
	Define user registration form (creating new user - public operation).
	It defines:
		attribute:
			fullname - User fullname
			username - User system name
			email - User email contact
			password - User password
			confirm - User password confirm
		method:
			None
	"""

	fullname = StringField("Fullname", validators=[Length(min=4, max=72)])
	username = StringField("Username", validators=[Length(min=4, max=32)])
	email = StringField(
		"Email Address",
		validators=[DataRequired(), Email(), Length(min=6, max=80)]
	)
	password = PasswordField(
		"Password", validators=[DataRequired(), Length(min=6, max=32)]
	)
	confirm = PasswordField(
		"Confirm password", validators=[DataRequired(), EqualTo("password")]
	)
