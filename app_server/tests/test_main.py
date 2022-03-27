# -*- coding: utf-8 -*-

'''
 Module
     test_main.py
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
     Define class TestMainBlueprint with attribute(s) and method(s).
     Define TestMainBlueprint for testing App.
'''

import sys
import unittest

try:
    from app_server.tests import BaseTestCase
except ImportError as error_message:
    MESSAGE = '\n{0}\n{1}\n'.format(__file__, error_message)
    sys.exit(MESSAGE)  # Force close python ATS ##############################

__author__ = 'Vladimir Roncevic'
__copyright__ = 'Copyright 2017, Free software to use and distributed it.'
__credits__ = ['Vladimir Roncevic']
__license__ = 'GNU General Public License (GPL)'
__version__ = '1.1.0'
__maintainer__ = 'Vladimir Roncevic'
__email__ = 'elektron.ronca@gmail.com'
__status__ = 'Updated'


class TestMainBlueprint(BaseTestCase):
    '''
        Define class TestMainBlueprint with attribute(s) and method(s).
        Define TestMainBlueprint for testing App.
        It defines:

            :attributes:
                | client - Client
            :methods:
                | test_index - Test index page
                | test_about - Test about page
                | test_404 - Test error page
    '''

    def test_index(self):
        '''
            Test index page

            :exceptions: None
        '''
        # Ensure Flask is setup.
        response = self.client.get('/', follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Welcome!', response.data)
        self.assertIn(b'Register/Login', response.data)

    def test_about(self):
        '''
            Test about page

            :exceptions: None
        '''
        # Ensure about route behaves correctly.
        response = self.client.get('/about', follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'About', response.data)

    def test_404(self):
        '''
            Test error page

            :exceptions: None
        '''
        # Ensure 404 error is handled.
        response = self.client.get('/404')
        self.assert404(response)
        self.assertTemplateUsed('errors/404.html')


if __name__ == '__main__':
    unittest.main()
