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
from flask import (
	session, render_template, url_for, redirect, flash, request
)
from flask_login import login_user

from app_server import bcrypt
from app_server.forms.user.login import UserLoginForm
from app_server.models.model_user import User

class Login(View):
	"""
	Define class Login with attribute(s) and method(s).
	View for login process.
	It defines:
		attribute:
			methods - Handler methods
		method:
			dispatch_request - Method view for login process
	"""

	methods = ["GET", "POST"]

	def dispatch_request(self):
		"""
		:return: Value of the view or error handler
		:rtype: View
		"""
		form = UserLoginForm(request.form)
		if form.validate_on_submit():
			user = User.query.filter_by(email=form.email.data).first()
			password_ok = bcrypt.check_password_hash(
				user.password, request.form.get("password")
			)
			if user and password_ok:
				login_user(user)
				flash("You are logged in. Welcome!", "success")
				session["logged_in"] = True
				if user.admin:
					return redirect(url_for("user.administration"))
				return redirect(url_for("user.members"))
			else:
				flash("Invalid email and/or password.", "danger")
				return render_template('user/login.html', form=form)
		return render_template(
			"user/login.html", title="Please Login", form=form
		)
