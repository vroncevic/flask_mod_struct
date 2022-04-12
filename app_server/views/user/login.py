# -*- coding: utf-8 -*-

'''
 Module
     login.py
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
     You should have received a copy of the GNU General Public License along
     with this program. If not, see <http://www.gnu.org/licenses/>.
 Info
     Define class Login with attribute(s) and method(s).
     Create view for login process.
'''

import sys

try:
    from flask.views import View
    from flask import (
        session, render_template, url_for, redirect, flash, request
    )
    from flask_login import login_user
    from app_server import bcrypt
    from app_server.forms.user.login import UserLoginForm
    from app_server.models.model_user import User
except ImportError as error_message:
    MESSAGE = '\n{0}\n{1}\n'.format(__file__, error_message)
    sys.exit(MESSAGE)  # Force close python ATS ##############################

__author__ = 'Vladimir Roncevic'
__copyright__ = 'Copyright 2017, Free software to use and distributed it.'
__credits__ = ['Vladimir Roncevic']
__license__ = 'GNU General Public License (GPL)'
__version__ = '1.3.0'
__maintainer__ = 'Vladimir Roncevic'
__email__ = 'elektron.ronca@gmail.com'
__status__ = 'Updated'


class Login(View):
    '''
        Define class Login with attribute(s) and method(s).
        Define view for login process.
        It defines:

            :attributes:
                | methods - Handler methods
            :methods:
                | dispatch_request - Method view for login process
    '''

    methods = ['GET', 'POST']

    def dispatch_request(self):
        '''
            Method view for login process

            :return: Value of the view or error handler
            :rtype: <View>
            :exceptions: None
        '''
        form = UserLoginForm(request.form)
        if form.validate_on_submit():
            user = User.query.filter_by(email=form.email.data).first()
            password_ok = bcrypt.check_password_hash(
                user.password, request.form.get('password')
            )
            if user and password_ok:
                login_user(user)
                flash('You are logged in. Welcome!', 'success')
                session['logged_in'] = True
                if user.admin:
                    return redirect(url_for('user.administration'))
                return redirect(url_for('user.members'))
            else:
                flash('Invalid email and/or password.', 'danger')
                return render_template('user/login.html', form=form)
        return render_template(
            'user/login.html', title='Please Login', form=form
        )
