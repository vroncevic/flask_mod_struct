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
from app_server.forms.user.edit import UserEdit

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
		form = UserEdit(request.form)
		if form.validate_on_submit():
			user = User.query.filter_by(username=username).first()
			user.fullname = request.form["fullname"]
			user.username = request.form["username"]
			user.email = request.form["email"]
			user.password = bcrypt.generate_password_hash(
				request.form["password"], app.config.get('BCRYPT_LOG_ROUNDS')
			)
			user.confirm = request.form["confirm"]
			if request.form["admin"] == "y":
				user.admin = True
			else:
				user.admin = False
			db.session.commit()
			return redirect(url_for("user.administration"))
		return render_template("user/edit.html", user=username, form=form)
