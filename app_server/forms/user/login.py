# -*- coding: utf-8 -*-

'''
 Module
     login.py
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
     Define class UserLoginForm with attribute(s) and method(s).
     Form for login user data.
'''

import sys

try:
    from flask_wtf import FlaskForm
    from wtforms import StringField, PasswordField
    from wtforms.validators import DataRequired, Email
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


class UserLoginForm(FlaskForm):
    '''
        Define class UserLoginForm with attribute(s) and method(s).
        Define user login form (by email and password).
        It defines:

            :attributes:
                | email - User contact email
                | password - User password
            :methods:
                | None
    '''

    email = StringField('Email Address', [DataRequired(), Email()])
    password = PasswordField('Password', [DataRequired()])
