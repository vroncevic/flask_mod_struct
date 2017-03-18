# encoding: utf-8
__author__ = "Vladimir Roncevic"
__copyright__ = "Copyright 2017, Free software to use and distributed it."
__credits__ = ["Vladimir Roncevic"]
__license__ = "GNU General Public License (GPL)"
__version__ = "1.0.0"
__maintainer__ = "Vladimir Roncevic"
__email__ = "elektron.ronca@gmail.com"
__status__ = "Updated"

from flask import Module, render_template

base = Module(__name__)

@base.route("/")
def home():
	return render_template("base/home.html")

@base.route("/contact/")
def contact():
	return render_template("base/contact.html")

@base.route("/about/")
def about():
	return render_template("base/about.html")
