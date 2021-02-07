# -*- coding: utf-8 -*-

"""
 Module
     __init__.py
 Copyright
     Copyright (C) 2017 Vladimir Roncevic <elektron.ronca@gmail.com>
     flask_mod_struct is free software: you can redistribute it and/or modify it
     under the terms of the GNU General Public License as published by the
     Free Software Foundation, either version 3 of the License, or
     (at your option) any later version.
     flask_mod_struct is distributed in the hope that it will be useful, but
     WITHOUT ANY WARRANTY; without even the implied warranty of
     MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
     See the GNU General Public License for more details.
     You should have received a copy of the GNU General Public License along
     with this program. If not, see <http://www.gnu.org/licenses/>.
 Info
     Defined url rule views.
"""

import sys

try:
    from flask import Module
    from app_server.views.user.login import Login
    from app_server.views.user.logout import Logout
    from app_server.views.user.register import Register
    from app_server.views.user.members import Members
    from app_server.views.user.administration import Administration
    from app_server.views.user.edit import Edit
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

user = Module(__name__)

user.add_url_rule("/login/", view_func=Login.as_view("login"))
user.add_url_rule(
    "/register/", view_func=Register.as_view("register")
)
user.add_url_rule("/logout/", view_func=Logout.as_view("logout"))
user.add_url_rule("/members/", view_func=Members.as_view("members"))
user.add_url_rule(
    "/administration/", view_func=Administration.as_view("administration")
)
user.add_url_rule("/edit/<username>", view_func=Edit.as_view("edit"))
