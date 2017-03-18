# encoding: utf-8
__author__ = "Vladimir Roncevic"
__copyright__ = "Copyright 2017, Free software to use and distributed it."
__credits__ = ["Vladimir Roncevic"]
__license__ = "GNU General Public License (GPL)"
__version__ = "1.0.0"
__maintainer__ = "Vladimir Roncevic"
__email__ = "elektron.ronca@gmail.com"
__status__ = "Updated"

from flask import Module, render_template, request, flash, redirect, url_for
from flask_login import login_user, login_required, logout_user

from app_server import db, bcrypt
from app_server.forms.user_login import UserLogin
from app_server.forms.user_register import UserRegister
from app_server.models.model_user import User

user = Module(__name__)

@user.route("/login/", methods=["GET", "POST"])
def login():
	form = UserLogin(request.form)
	if form.validate_on_submit():
		user = User.query.filter_by(email=form.email.data).first()
		password_ok = bcrypt.check_password_hash(
			user.password, request.form["password"]
		)
		if user and password_ok:
			login_user(user)
			flash("You are logged in. Welcome!", "success")
			return redirect(url_for("user.members"))
		else:
			flash("Invalid email and/or password.", "danger")
			return render_template('user/login.html', form=form)
	return render_template("user/login.html", title="Please Login", form=form)

@user.route("/register/", methods=["GET", "POST"])
def register():
	form = UserRegister(request.form)
	if form.validate_on_submit():
		user = User(
			fullname=form.fullname.data, username=form.username.data,
			email=form.email.data, password=form.password.data
		)
		db.session.add(user)
		db.session.commit()
		login_user(user)
		flash("Thank you for registering.", "success")
		return redirect(url_for("user.members"))
	return render_template("user/register.html", form=form)

@user.route("/logout/")
@login_required
def logout():
	logout_user()
	flash("You were logged out. Bye!", "success")
	return redirect(url_for("base.home"))

@user.route("/members/")
@login_required
def members():
	return render_template("user/members.html")

@user.route("/administration/")
@login_required
def administration():
	return render_template("user/administration.html")
