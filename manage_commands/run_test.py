# encoding: utf-8
__author__ = "Vladimir Roncevic"
__copyright__ = "Copyright 2017, Free software to use and distributed it."
__credits__ = ["Vladimir Roncevic"]
__license__ = "GNU General Public License (GPL)"
__version__ = "1.0.0"
__maintainer__ = "Vladimir Roncevic"
__email__ = "elektron.ronca@gmail.com"
__status__ = "Updated"

from flask_script import Command
import unittest

class RunTest(Command):
	"""
	Define class RunTest with attribute(s) and method(s).
	Run tests.
	It defines:
		attribute:
			None
		method:
			__init__ - Initial constructor
			run - Run tests
	"""

	def __init__(self):
		super(RunTest, self).__init__()

	def run(self):
		tests = unittest.TestLoader().discover(
			"app_server/tests", pattern="test*.py"
		)
		result = unittest.TextTestRunner(verbosity=2).run(tests)
		if result.wasSuccessful():
			return 0
		return 1
