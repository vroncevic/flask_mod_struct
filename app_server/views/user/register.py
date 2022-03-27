# -*- coding: utf-8 -*-

'''
 Module
     register.py
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
     Define class Register with attribute(s) and method(s).
     View for register user data.
'''

import sys

try:
    from flask.views import View
    from flask import (
        session, render_template, url_for, redirect, flash, request
    )
    from flask_login import login_user
    from app_server import db
    from app_server.forms.user.register import UserRegisterForm
    from app_server.models.model_user import User
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


class Register(View):
    '''
        Define class Register with attribute(s) and method(s).
        Define register view for new user (standard user).
        It defines:

            :attributes:
                | methods - Handler methods
            :methods:
                | dispatch_request - Method view for user register process
    '''

    methods = ['GET', 'POST']

    def dispatch_request(self):
        '''
        Method view for user register process

        :return: Value of the view or error handler
        :rtype: <View>
        :exceptions: None
        '''
        form = UserRegisterForm(request.form)
        if form.validate_on_submit():
            user = User(
                username=form.username.data, password=form.password.data
            )
            user.fullname = form.fullname.data
            user.email = form.email.data
            db.session.add(user)
            db.session.commit()
            login_user(user)
            session['logged_in'] = True
            flash('Thank you for registering.', 'success')
            return redirect(url_for('user.members'))
        return render_template('user/register.html', form=form)
