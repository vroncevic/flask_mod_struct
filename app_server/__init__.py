# -*- coding: utf-8 -*-

"""
 Module
     __init__.py
 Copyright
     Copyright (C) 2017 Vladimir Roncevic <elektron.ronca@gmail.com>
     flask_mod_struct is free software: you can redistribute it and/or
     modify it under the terms of the GNU General Public License as published
     by the Free Software Foundation, either version 3 of the License, or
     (at your option) any later version.
     flask_mod_struct is distributed in the hope that it will be useful,
     but WITHOUT ANY WARRANTY; without even the implied warranty of
     MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
     See the GNU General Public License for more details.
     You should have received a copy of the GNU General Public License along
     with this program. If not, see <http://www.gnu.org/licenses/>.
 Info
     Define Flask application with default error pages.
"""

import os
import sys

try:
    from flask import Flask, render_template
    from flask_bcrypt import Bcrypt
    from flask_bootstrap import Bootstrap
    from flask_debugtoolbar import DebugToolbarExtension
    from flask_login import LoginManager
    from flask_sqlalchemy import SQLAlchemy
    from flask_mail import Mail
except ImportError as error_message:
    MESSAGE = "\n{0}\n{1}\n".format(__file__, error_message)
    sys.exit(MESSAGE)  # Force close python ATS ##############################

app = Flask(__name__, template_folder="templates", static_folder="static")
app_settings = os.getenv(
    "APP_SETTINGS",
    "app_server.configuration.development_config.DevelopmentConfig"
)
app_settings_database = os.getenv(
    "APP_SETTINGS_DATABASE",
    "app_server.configuration.database.development_config.DevelopmentConfig"
)
app_settings_mail = os.getenv(
    "APP_SETTINGS_MAIL",
    "app_server.configuration.mail.development_config.DevelopmentConfig"
)
app.config.from_object(app_settings)
app.config.from_object(app_settings_database)
app.config.from_object(app_settings_mail)
login_manager = LoginManager()
login_manager.init_app(app)
bcrypt = Bcrypt(app)
toolbar = DebugToolbarExtension(app)
bootstrap = Bootstrap(app)
mail = Mail(app)
db = SQLAlchemy(app)

try:
    from app_server.views.base import base
    from app_server.views.user import user
except ImportError as error_message:
    MESSAGE = "\n{0}\n{1}\n".format(__file__, error_message)
    sys.exit(MESSAGE)  # Force close python ATS ##############################

app.register_module(base)
app.register_module(user)

try:
    from app_server.models.model_user import User
except ImportError as error_message:
    MESSAGE = "\n{0}\n{1}\n".format(__file__, error_message)
    sys.exit(MESSAGE)  # Force close python ATS ##############################

__author__ = "Vladimir Roncevic"
__copyright__ = "Copyright 2017, Free software to use and distributed it."
__credits__ = ["Vladimir Roncevic"]
__license__ = "GNU General Public License (GPL)"
__version__ = "1.1.0"
__maintainer__ = "Vladimir Roncevic"
__email__ = "elektron.ronca@gmail.com"
__status__ = "Updated"

login_manager.login_view = "user.login"
login_manager.login_message_category = "danger"

@login_manager.user_loader
def load_user(user_id):
    """
        Loading user in context of login manager.

        :return: Loaded user
        :rtype: <User>
        :exceptions: None
    """
    return User.query.filter(User.id == int(user_id)).first()

@app.errorhandler(401)
def forbidden_page(error):
    """
        Unauthorized client error status response.

        :return: Unauthorized client page, response code
        :rtype: <str>, <int>
        :exceptions: None
    """
    return render_template("errors/401.html"), 401

@app.errorhandler(403)
def forbidden_page(error):
    """
        Forbidden client error status response.

        :return: Forbidden client page, response code
        :rtype: <str>, <int>
        :exceptions: None
    """
    return render_template("errors/403.html"), 403

@app.errorhandler(404)
def page_not_found(error):
    """
        Server Not Found.

        :return: Server not found page, response code
        :rtype: <str>, <int>
        :exceptions: None
    """
    return render_template("errors/404.html"), 404

@app.errorhandler(500)
def server_error_page(error):
    """
        Defining internal server error response.

        :return: Internal server error page, response code
        :rtype: <str>, <int>
        :exceptions: None
    """
    return render_template("errors/500.html"), 500
