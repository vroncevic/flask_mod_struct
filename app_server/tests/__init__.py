# encoding: utf-8
__author__ = "Vladimir Roncevic"
__copyright__ = "Copyright 2017, Free software to use and distributed it."
__credits__ = ["Vladimir Roncevic"]
__license__ = "GNU General Public License (GPL)"
__version__ = "1.0.0"
__maintainer__ = "Vladimir Roncevic"
__email__ = "elektron.ronca@gmail.com"
__status__ = "Updated"

from flask_testing import TestCase

from app_server import app, db, bcrypt
from app_server.models.model_user import User

class BaseTestCase(TestCase):

	def create_app(self):
		app.config.from_object("app_server.configuration.TestConfig")
		return app

	def setUp(self):
		db.create_all()
		admin_password = bcrypt.generate_password_hash(
			"admin", app.config.get('BCRYPT_LOG_ROUNDS')
		)
		user = User(
			username=admin_password, password="admin", admin=True
		)
		user.fullname="Flask Administrator"
		user.email="admin@admin.com"
		db.session.add(user)
		db.session.commit()

	def tearDown(self):
		db.session.remove()
		db.drop_all()
