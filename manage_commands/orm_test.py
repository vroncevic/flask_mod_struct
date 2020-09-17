# -*- coding: utf-8 -*-

"""
 Module
     orm_test.py
 Copyright
     Copyright (C) 2017 Vladimir Roncevic <elektron.ronca@gmail.com>
     manage_flask is free software: you can redistribute it and/or modify it
     under the terms of the GNU General Public License as published by the
     Free Software Foundation, either version 3 of the License, or
     (at your option) any later version.
     manage_flask is distributed in the hope that it will be useful, but
     WITHOUT ANY WARRANTY; without even the implied warranty of
     MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
     See the GNU General Public License for more details.
     You should have received a copy of the GNU General Public License along
     with this program. If not, see <http://www.gnu.org/licenses/>.
 Info
     Define class ORMTest with attribute(s) and method(s).
     Create initial data and insert to database.
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
    from flask_script import Command
    from app_server.tests.sqlalchemy_query import SQLAlchemyQuery
except ImportError as error:
    MESSAGE = "\n{0}\n{1}\n".format(__file__, error)
    sys.exit(MESSAGE)  # Force close python ATS ##############################


class ORMTest(Command):
    """
        Define class ORMTest with attribute(s) and method(s).
        Command for ORM tests.
        It defines:

            :attributes:
                | __query - Run query tests
            :methods:
                | __init__ - Initial constructor
                | run - Run queries.
    """

    def __init__(self):
        """
            Initial constructor

            :exceptions: None
        """
        super(ORMTest, self).__init__()
        self.__query = SQLAlchemyQuery()

    def run(self):
        """
            Run testes

            :return: 0 for success else 1
            :rtype: <int>
            :exceptions: None
        """
        print("Run ORM tests")
        self.__query.query_all()
        print("Done")
        return 0
