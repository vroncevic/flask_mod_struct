# encoding: utf-8
__author__ = "Vladimir Roncevic"
__copyright__ = "Copyright 2017, Free software to use and distributed it."
__credits__ = ["Vladimir Roncevic"]
__license__ = "GNU General Public License (GPL)"
__version__ = "1.0.0"
__maintainer__ = "Vladimir Roncevic"
__email__ = "elektron.ronca@gmail.com"
__status__ = "Updated"

from app_server.configuration.development_config import DevelopmentConfig
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

class SQLAlchemyBaseQuery(object):
	"""
	Define class SQLAlchemyBaseQuery with attribute(s) and method(s).
	Create database engine.
	It defines:
		attribute:
			Base - Base class for declarative class definitions
			Engine - Starting point for any SQLAlchemy application
			Session - Connection session
		method:
			None
	"""

	Base = declarative_base()
	Engine = create_engine(DevelopmentConfig.SQLALCHEMY_DATABASE_URI)
	Session = sessionmaker(bind=Engine)
