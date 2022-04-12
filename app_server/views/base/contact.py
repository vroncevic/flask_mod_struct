# -*- coding: utf-8 -*-

'''
 Module
     contact.py
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
     Define class Contact with attribute(s) and method(s).
     View for contact user data.
'''

import sys

try:
    from flask.views import View
    from flask import render_template, request, flash
    from flask_mail import Message
    from app_server import app, mail
    from app_server.forms.base.contact import ContactForm
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


class Contact(View):
    '''
        Define class Contact with attribute(s) and method(s).
        Define view for contact page.
        It defines:

            :attributes:
                | methods - Handler methods
            :methods:
                | dispatch_request - Method view for contact page
    '''

    methods = ['GET', 'POST']

    def dispatch_request(self):
        '''
            Method view for contact page

            :return: Value of the view or error handler
            :rtype: <View>
            :exceptions: None
        '''
        form = ContactForm(request.form)
        if form.validate_on_submit():
            subject = request.form.get('subject')
            message = request.form.get('message')
            name = request.form.get('name')
            email = request.form.get('email')
            msg = Message(
                subject=subject,
                sender=app.config.get('MAIL_USERNAME'),
                recipients=[app.config.get('MAIL_RECIPIENT')]
            )
            msg.body = '{0}\n{1}\n{2}'.format(message, name, email)
            mail.send(msg)
            flash('Message sent!', 'success')
        return render_template('base/contact.html', form=form)
