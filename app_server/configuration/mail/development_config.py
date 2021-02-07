# -*- coding: utf-8 -*-

"""
 Module
     development_config.py
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
     Define class DevelopmentConfig with attribute(s) and method(s).
     Define mail development configuration.
"""

import sys

try:
    from app_server.configuration.mail import BaseConfig
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


class DevelopmentConfig(BaseConfig):
    """
        Define class DevelopmentConfig with attribute(s) and method(s).
        Define mail development configuration.
        It defines:

            :attributes:
                | MAIL_USERNAME - Mail username
                | MAIL_PASSWORD - Mail password
                | MAIL_RECIPIENT - Mail username
            :methods:
                | None
    """

    MAIL_USERNAME = "g.sender@gmail.com"
    MAIL_PASSWORD = "g_sender_password"
    MAIL_RECIPIENT = "m.receiver@outlook.com"
