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
from flask import render_template, url_for, redirect, flash, request
from flask_login import login_user, session

from app_server import db
from app_server.forms.user.register import UserRegisterForm
from app_server.models.model_user import User

class Register(View):
	"""
	Define class Register with attribute(s) and method(s).
	Register view for new user (standard user).
	It defines:
		attribute:
			methods - Handler methods
		method:
			dispatch_request - Method view for user register process
	"""

	methods = ["GET", "POST"]

	def dispatch_request(self):
		"""
		:return: Value of the view or error handler
		:rtype: View
		"""
		form = UserRegisterForm(request.form)
		if form.validate_on_submit():
			user = User(
				username=form.username.data, password=form.password.data
			)
			user.fullname=form.fullname.data
			user.email=form.email.data
			db.session.add(user)
			db.session.commit()
			login_user(user)
			session["logged_in"] = True
			flash("Thank you for registering.", "success")
			return redirect(url_for("user.members"))
		return render_template("user/register.html", form=form)
