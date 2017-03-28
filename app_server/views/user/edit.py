# encoding: utf-8
__author__ = "Vladimir Roncevic"
__copyright__ = "Copyright 2017, Free software to use and distributed it."
__credits__ = ["Vladimir Roncevic"]
__license__ = "GNU General Public License (GPL)"
__version__ = "1.0.0"
__maintainer__ = "Vladimir Roncevic"
__email__ = "elektron.ronca@gmail.com"
__status__ = "Updated"

from flask.views import MethodView
from flask import render_template, request, url_for, redirect
from flask_login import login_required

from app_server import app, db, bcrypt
from app_server.models.model_user import User
from app_server.forms.user.edit import UserEditForm

class Edit(MethodView):
	"""
	Define class Edit with attribute(s) and method(s).
	View for edit user data.
	It defines:
		attribute:
			decorators - List of decorators
			methods - Handler methods
		method:
			dispatch_request - Method view for edit user data
	"""

	decorators = [login_required]
	methods = ["GET", "POST"]

	def dispatch_request(self, username):
		"""
		:param username: System username
		:type username: str
		:return: Value of the view or error handler
		:rtype:
		"""
		user = User.query.filter_by(username=username).first()
		form = UserEditForm(request.form)
		form.fullname.data = user.fullname
		form.username.data = user.username
		form.email.data = user.email
		if user.admin:
			form.admin.data = True
		else:
			form.admin.data = False
		if form.validate_on_submit():
			user.fullname = request.form.get("fullname")
			user.username = request.form.get("username")
			user.email = request.form.get("email")
			if request.form.get("password"):
				user.password = bcrypt.generate_password_hash(
					request.form.get("password"),
					app.config.get("BCRYPT_LOG_ROUNDS")
				)
			if request.form.get("admin"):
				user.admin = True
			else:
				user.admin = False
			db.session.commit()
			return redirect(url_for("user.administration"))
		return render_template("user/edit.html", user=username, form=form)
