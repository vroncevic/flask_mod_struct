# -*- coding: utf-8 -*-

"""
 Module
     members.py
 Copyright
     Copyright (C) 2017 Vladimir Roncevic <elektron.ronca@gmail.com>
     flask_mod_struct is free software: you can redistribute it and/or
     modify it under the terms of the GNU General Public License as
     published by the Free Software Foundation, either version 3 of
     the License, or (at your option) any later version.
     flask_mod_struct is distributed in the hope that it will be useful,
     but WITHOUT ANY WARRANTY; without even the implied warranty of
     MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
     See the GNU General Public License for more details.
     You should have received a copy of the GNU General Public License
     along with this program. If not, see <http://www.gnu.org/licenses/>.
 Info
     Define class Members with attribute(s) and method(s).
     Define view for member list (list of standard users).
"""

import sys

try:
    from flask.views import View
    from flask import render_template
    from flask_login import login_required
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


class Members(View):
    """
        Define class Members with attribute(s) and method(s).
        Define view for member list (list of standard users).
        It defines:

            :attributes:
                | decorators - List of decorators
            :methods:
                | dispatch_request - View for list of users (without admin)
    """

    decorators = [login_required]

    def dispatch_request(self):
        """
            View for list of users (without admin)

            :return: Value of the view or error handler
            :rtype: <View>
            :exceptions: None
        """
        data_view = User.query.filter(User.id != 1)
        return render_template("user/members.html", data=data_view)
