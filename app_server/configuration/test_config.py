# -*- coding: utf-8 -*-

"""
 Module
     test_config.py
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
     Define class TestConfig with attribute(s) and method(s).
"""

__author__ = "Vladimir Roncevic"
__copyright__ = "Copyright 2017, Free software to use and distributed it."
__credits__ = ["Vladimir Roncevic"]
__license__ = "GNU General Public License (GPL)"
__version__ = "1.0.0"
__maintainer__ = "Vladimir Roncevic"
__email__ = "elektron.ronca@gmail.com"
__status__ = "Updated"

import sys

try:
    from app_server.configuration import BaseConfig
except ImportError as error:
    MESSAGE = "\n{0}\n{1}\n".format(__file__, error)
    sys.exit(MESSAGE)  # Force close python ATS ##############################


class TestConfig(BaseConfig):
    """
        Define class TestConfig with attribute(s) and method(s).
        Define test configuration.
        It defines:

            :attributes:
                | DEBUG - Enable/Disable debug option
                | WTF_CSRF_ENABLED - Secure forms
                | DEBUG_TB_ENABLED - Flask debug toolbar's
                | DEBUG_TB_INTERCEPT_REDIRECTS - Should intercept redirects?
                | BCRYPT_LOG_ROUNDS - for bcrypt hashing utilities
            :methods:
                | None
    """

    DEBUG = True
    WTF_CSRF_ENABLED = False
    DEBUG_TB_ENABLED = True
    DEBUG_TB_INTERCEPT_REDIRECTS = True
    BCRYPT_LOG_ROUNDS = 4
