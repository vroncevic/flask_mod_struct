# encoding: utf-8
__author__ = "Vladimir Roncevic"
__copyright__ = "Copyright 2017, Free software to use and distributed it."
__credits__ = ["Vladimir Roncevic"]
__license__ = "GNU General Public License (GPL)"
__version__ = "1.0.0"
__maintainer__ = "Vladimir Roncevic"
__email__ = "elektron.ronca@gmail.com"
__status__ = "Updated"

import os

from flask import Flask, render_template
from flask_bcrypt import Bcrypt
from flask_bootstrap import Bootstrap
from flask_debugtoolbar import DebugToolbarExtension
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy

app = Flask(
	__name__,
	template_folder="templates",
	static_folder="static"
)

app_settings = os.getenv(
	"APP_SETTINGS",
	"app_server.configuration.development_config.DevelopmentConfig"
)

app.config.from_object(app_settings)
login_manager = LoginManager()
login_manager.init_app(app)
bcrypt = Bcrypt(app)
toolbar = DebugToolbarExtension(app)
bootstrap = Bootstrap(app)
db = SQLAlchemy(app)

from app_server.views.base import base
from app_server.views.user import user

app.register_module(base)
app.register_module(user)

from app_server.models.model_user import User

login_manager.login_view = "user.login"
login_manager.login_message_category = "danger"

@login_manager.user_loader
def load_user(user_id):
	return User.query.filter(User.id == int(user_id)).first()

@app.errorhandler(401)
def forbidden_page(error):
	return render_template("errors/401.html"), 401

@app.errorhandler(403)
def forbidden_page(error):
	return render_template("errors/403.html"), 403

@app.errorhandler(404)
def page_not_found(error):
	return render_template("errors/404.html"), 404

@app.errorhandler(500)
def server_error_page(error):
	return render_template("errors/500.html"), 500
