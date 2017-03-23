# encoding: utf-8
__author__ = "Vladimir Roncevic"
__copyright__ = "Copyright 2017, Free software to use and distributed it."
__credits__ = ["Vladimir Roncevic"]
__license__ = "GNU General Public License (GPL)"
__version__ = "1.0.0"
__maintainer__ = "Vladimir Roncevic"
__email__ = "elektron.ronca@gmail.com"
__status__ = "Updated"

from flask import Module

from app_server.views.base.home import Home
from app_server.views.base.contact import Contact
from app_server.views.base.about import About

base = Module(__name__)

base.add_url_rule("/", view_func=Home.as_view("home"))
base.add_url_rule("/contact/", view_func=Contact.as_view("contact"))
base.add_url_rule("/about/", view_func=About.as_view("about"))
