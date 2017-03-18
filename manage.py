# encoding: utf-8
__author__ = "Vladimir Roncevic"
__copyright__ = "Copyright 2017, Free software to use and distributed it."
__credits__ = ["Vladimir Roncevic"]
__license__ = "GNU General Public License (GPL)"
__version__ = "1.0.0"
__maintainer__ = "Vladimir Roncevic"
__email__ = "elektron.ronca@gmail.com"
__status__ = "Updated"

import coverage
from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager
from manage_commands.create_database import CreateDatabase
from manage_commands.drop_database import DropDatabase
from manage_commands.create_data import CreateData
from manage_commands.create_superuser import CreateSuperUser
from manage_commands.run_coverage import RunCoverage
from manage_commands.run_test import RunTest

COV = coverage.coverage(
	branch=True,
	include="app_server/*",
	omit=[
		"app_server/tests/*",
		"app_server/configuration/testing_config.py",
		"app_server/*/__init__.py"
	]
)

COV.start()

from app_server import app, db

migrate = Migrate(app, db)
manager = Manager(app)
manager.add_command("db", MigrateCommand)
manager.add_command("create_db", CreateDatabase(db))
manager.add_command("drop_db", DropDatabase(db))
manager.add_command("create_data", CreateData(db))
manager.add_command("createsuperuser", CreateSuperUser(db))
manager.add_command("test", RunTest())
manager.add_command("coverage", RunCoverage(COV))

# python manage.py create_db
# python manage.py db init
# python manage.py db migrate
# python manage.py createsuperuser
# python manage.py create_data
# python manage.py runserver

if __name__ == "__main__":
	manager.run()
