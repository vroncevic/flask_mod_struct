# -*- coding: utf-8 -*-

'''
 Module
     production_config.py
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
     Define class ProductionConfig with attribute(s) and method(s).
     Define production configuration.
'''

import sys

try:
    from app_server.configuration import BaseConfig
except ImportError as error_message:
    MESSAGE = '\n{0}\n{1}\n'.format(__file__, error_message)
    sys.exit(MESSAGE)  # Force close python ATS ##############################

__author__ = 'Vladimir Roncevic'
__copyright__ = 'Copyright 2017, Free software to use and distributed it.'
__credits__ = ['Vladimir Roncevic']
__license__ = 'GNU General Public License (GPL)'
__version__ = '1.3.0'
__maintainer__ = 'Vladimir Roncevic'
__email__ = 'elektron.ronca@gmail.com'
__status__ = 'Updated'


class ProductionConfig(BaseConfig):
    '''
        Define class DevelopmentConfig with attribute(s) and method(s).
        Define production configuration.
        It defines:

            :attributes:
                | DEBUG - Enable/Disable debug option
                | WTF_CSRF_ENABLED - Secure forms
                | DEBUG_TB_ENABLED - Flask debug toolbar's
                | DEBUG_TB_INTERCEPT_REDIRECTS - Should intercept redirects?
                | BCRYPT_LOG_ROUNDS - for bcrypt hashing utilities
            :methods:
                | None
    '''

    DEBUG = False
    WTF_CSRF_ENABLED = True
    DEBUG_TB_ENABLED = False
    DEBUG_TB_INTERCEPT_REDIRECTS = False
    BCRYPT_LOG_ROUNDS = 4
