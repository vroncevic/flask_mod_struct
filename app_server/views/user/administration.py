# -*- coding: utf-8 -*-

'''
 Module
     administration.py
 Copyright
     Copyright (C) 2017 Vladimir Roncevic <elektron.ronca@gmail.com>
     flask_mod_struct is free software: you can redistribute it and/or
     modify it under the terms of the GNU General Public License as
     published by the Free Software Foundation, either version 3 of
     the License, or (at your option) any later version.
     flask_mod_struct is distributed in the hope that it will be useful, but
     WITHOUT ANY WARRANTY; without even the implied warranty of
     MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
     See the GNU General Public License for more details.
     You should have received a copy of the GNU General Public License along
     with this program. If not, see <http://www.gnu.org/licenses/>.
 Info
     Define class Administration with attribute(s) and method(s).
     Create Administration page.
'''

import sys

try:
    from flask.views import View
    from flask import render_template
    from flask_login import login_required
    from app_server import db
    from app_server.models.model_user import User
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


class Administration(View):
    '''
        Define class Administration with attribute(s) and method(s).
        Define administration view (list of all users).
        It defines:

        :attributes:
            | decorators - List of decorators
        :methods:
            | dispatch_request - Implement dispatch request
    '''

    decorators = [login_required]

    def dispatch_request(self):
        '''
            Implement dispatch request

            :return: Value of the view or error handler
            :rtype: <View>
            :exceptions: None
        '''
        data_view = db.session.query(User).all()
        return render_template('user/administration.html', data=data_view)
