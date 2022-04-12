# -*- coding: utf-8 -*-

'''
 Module
     sqlalchemy_query.py
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
     Define class SQLAlchemyQuery with attribute(s) and method(s).
     Create session and do query.
'''

import sys

try:
    from app_server.tests.base_query import SQLAlchemyBaseQuery
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


class SQLAlchemyQuery(object):
    '''
        Define class SQLAlchemyQuery with attribute(s) and method(s).
        Create session and do query.
        It defines:

            :attributes:
                | __session - Session maker
            :methods:
                | __init__ - Initial constructor
                | query_all - Query all
    '''

    def __init__(self):
        '''
            Initial constructor

            :exceptions: None
        '''
        self.__session = SQLAlchemyBaseQuery.Session()

    def query_all(self):
        '''
            Query all

            :exceptions: None
        '''
        for user in self.__session.query(User).all():
            print(user.fullname, user.username, user.email, user.admin)
