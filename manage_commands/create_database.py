# -*- coding: utf-8 -*-

'''
 Module
     create_database.py
 Copyright
     Copyright (C) 2017 Vladimir Roncevic <elektron.ronca@gmail.com>
     flask_mod_struct is free software: you can redistribute it and/or modify
     it under the terms of the GNU General Public License as published by the
     Free Software Foundation, either version 3 of the License, or
     (at your option) any later version.
     flask_mod_struct is distributed in the hope that it will be useful, but
     WITHOUT ANY WARRANTY; without even the implied warranty of
     MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
     See the GNU General Public License for more details.
     You should have received a copy of the GNU General Public License along
     with this program. If not, see <http://www.gnu.org/licenses/>.
 Info
     Define class CreateDatabase with attribute(s) and method(s).
     Create database by defined models.
'''

import sys

try:
    from flask_script import Command
except ImportError as error_message:
    MESSAGE = '\n{0}\n{1}\n'.format(__file__, error_message)
    sys.exit(MESSAGE)  # Force close python ATS ##############################

__author__ = 'Vladimir Roncevic'
__copyright__ = 'Copyright 2017, Free software to use and distributed it.'
__credits__ = ['Vladimir Roncevic']
__license__ = 'GNU General Public License (GPL)'
__version__ = '1.4.0'
__maintainer__ = 'Vladimir Roncevic'
__email__ = 'elektron.ronca@gmail.com'
__status__ = 'Updated'


class CreateDatabase(Command):
    '''
        Define class CreateDatabase with attribute(s) and method(s).
        Create database by defined models.
        It defines:

            :attributes:
                | __db - SQLAlchemy integration object
            :methods:
                | __init__ - Initial constructor
                | run - Create database with tables.
    '''

    def __init__(self, db):
        '''
            Initial constructor.

            :param db: SQLAlchemy integration object
            :type db: <SQLAlchemy>
            :exceptions: None
        '''
        super(CreateDatabase, self).__init__()
        self.__db = db

    def run(self):
        '''
            Create database with tables.

            :return: 0
            :rtype: <int>
            :exceptions: None
        '''
        print('Create database/tables')
        self.__db.create_all()
        print('Done')
        return 0
