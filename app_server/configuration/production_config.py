# encoding: utf-8
__author__ = "Vladimir Roncevic"
__copyright__ = "Copyright 2017, Free software to use and distributed it."
__credits__ = ["Vladimir Roncevic"]
__license__ = "GNU General Public License (GPL)"
__version__ = "1.0.0"
__maintainer__ = "Vladimir Roncevic"
__email__ = "elektron.ronca@gmail.com"
__status__ = "Updated"

class ProductionConfig(object):
	"""
	Define class ProductionConfig with attribute(s) and method(s).
	Production configuration class.
	It defines:
		attribute:
			SECRET_KEY - Production key for session accessing
			DEBUG - Enable/Disable debug option
			SQLALCHEMY_DATABASE_URI - Set DB URI
			DEBUG_TB_ENABLED - Flask debug toolbar's
		method:
			None
	"""

	SECRET_KEY = "my_precious"
	DEBUG = False
	SQLALCHEMY_DATABASE_URI = "postgresql://localhost/example"
	DEBUG_TB_ENABLED = False
