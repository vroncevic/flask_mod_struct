# -*- coding: utf-8 -*-

'''
 Module
     manage.py
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
     Define manage routines for Flask App.
     Main entry point of Flask App.
'''

import sys

try:
    from flask_migrate import Migrate, MigrateCommand
    from flask_script import Manager
    from manage_commands.create_database import CreateDatabase
    from manage_commands.drop_database import DropDatabase
    from manage_commands.create_data import CreateData
    from manage_commands.create_superuser import CreateSuperUser
    from manage_commands.run_coverage import RunCoverage
    from app_server import app, db
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

migrate = Migrate(app, db)
manager = Manager(app)
manager.add_command('db', MigrateCommand)
manager.add_command('create_db', CreateDatabase(db))
manager.add_command('drop_db', DropDatabase(db))
manager.add_command('create_data', CreateData(db))
manager.add_command('createsuperuser', CreateSuperUser(db))

# python manage.py create_db
# python manage.py db init
# python manage.py db migrate
# python manage.py createsuperuser
# python manage.py create_data
# python manage.py runserver

if __name__ == '__main__':
    manager.run()
