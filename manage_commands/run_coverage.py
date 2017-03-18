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
from os.path import dirname, abspath, join
import unittest

class RunCoverage(Command):
	"""
	Define class RunCoverage with attribute(s) and method(s).
	Create coverage reports.
	It defines:
		attribute:
			db - Coverage integration object
		method:
			__init__ - Initial constructor
			run - Create coverage reports
	"""

	def __init__(self, cov):
		"""
		:param cov: Coverage integration object
		:type: Coverage
		"""
		super(RunCoverage, self).__init__()
		self.cov = cov

	def run(self):
		tests = unittest.TestLoader().discover("app_server/tests")
		result = unittest.TextTestRunner(verbosity=2).run(tests)
		if result.wasSuccessful():
			self.cov.stop()
			self.cov.save()
			print("Coverage Summary:")
			self.cov.report()
			basedir = abspath(dirname(__file__))
			coverage_dir = join(basedir, "tmp/coverage")
			self.cov.html_report(directory=coverage_dir)
			print("HTML version: file://{0}/index.html".format(coverage_dir))
			self.cov.erase()
			return 0
		return 1
