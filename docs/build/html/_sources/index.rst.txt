Flask Module Structured Framework
----------------------------------

**flask_mod_struct** is framework for Flask web apps.

Developed in `python <https://www.python.org/>`_ code: **100%**.

The README is used to introduce the modules and provide instructions on
how to install the modules, any machine dependencies it may have and any
other information that should be provided before the modules are installed.

|Python package| |GitHub issues| |Documentation Status| |GitHub contributors|

.. |Python package| image:: https://github.com/vroncevic/flask_mod_struct/workflows/Python%20package%20flask_mod_struct/badge.svg
   :target: https://github.com/vroncevic/flask_mod_struct/workflows/Python%20package%20flask_mod_struct/badge.svg?branch=master

.. |GitHub issues| image:: https://img.shields.io/github/issues/vroncevic/flask_mod_struct.svg
   :target: https://github.com/vroncevic/flask_mod_struct/issues

.. |GitHub contributors| image:: https://img.shields.io/github/contributors/vroncevic/flask_mod_struct.svg
   :target: https://github.com/vroncevic/flask_mod_struct/graphs/contributors

.. |Documentation Status| image:: https://readthedocs.org/projects/flask_mod_struct/badge/?version=latest
   :target: https://flask_mod_struct.readthedocs.io/projects/flask_mod_struct/en/latest/?badge=latest

.. toctree::
   :maxdepth: 4
   :caption: Contents:

   self

Installation
-------------

Navigate to release `page`_ download and extract release archive.

.. _page: https://github.com/vroncevic/flask_mod_struct/releases

To install this set of modules type the following:

.. code-block:: bash

    tar xvzf flask_mod_struct-x.y.z.tar.gz
    cd flask_mod_struct-x.y.z/
    pip install -r requirements.txt
    cp manage.py /FlaskApp/
    cp -R /manage_commands/ /FlaskApp/
    cp -R /app_server/ /Flask/

Dependencies
-------------

**flask_mod_struct** requires next modules and libraries:

* Flask
* Flask-Migrate
* Flask-Script
* coverage
* WTForms
* Flask-Login
* Flask-BCrypt
* Flask-Bootstrap
* Flask-DebugToolbar
* Flask-SQLAlchemy
* Flask-Testing
* Flask-WTF

Library structure
------------------

**flask_mod_struct** is based on OOP:

Framework structure:

.. code-block:: bash

    .
    ├── app_server/
    │   ├── configuration/
    │   │   ├── database/
    │   │   │   ├── development_config.py
    │   │   │   ├── __init__.py
    │   │   │   ├── production_config.py
    │   │   │   └── test_config.py
    │   │   ├── development_config.py
    │   │   ├── __init__.py
    │   │   ├── mail/
    │   │   │   ├── development_config.py
    │   │   │   ├── __init__.py
    │   │   │   ├── production_config.py
    │   │   │   └── test_config.py
    │   │   ├── production_config.py
    │   │   └── test_config.py
    │   ├── forms/
    │   │   ├── base/
    │   │   │   ├── contact.py
    │   │   │   └── __init__.py
    │   │   ├── __init__.py
    │   │   └── user/
    │   │       ├── edit.py
    │   │       ├── __init__.py
    │   │       ├── login.py
    │   │       └── register.py
    │   ├── __init__.py
    │   ├── models/
    │   │   ├── __init__.py
    │   │   └── model_user.py
    │   ├── static/
    │   │   ├── base.css
    │   │   └── favicon.ico
    │   ├── templates/
    │   │   ├── base/
    │   │   │   ├── about.html
    │   │   │   ├── contact.html
    │   │   │   └── home.html
    │   │   ├── _base.html
    │   │   ├── errors/
    │   │   │   ├── 401.html
    │   │   │   ├── 403.html
    │   │   │   ├── 404.html
    │   │   │   └── 500.html
    │   │   ├── footer.html
    │   │   ├── header.html
    │   │   └── user/
    │   │       ├── administration.html
    │   │       ├── edit.html
    │   │       ├── login.html
    │   │       ├── members.html
    │   │       └── register.html
    │   ├── tests/
    │   │   ├── base_query.py
    │   │   ├── helpers.py
    │   │   ├── __init__.py
    │   │   ├── sqlalchemy_query.py
    │   │   ├── test_config.py
    │   │   ├── test_main.py
    │   │   └── test_user.py
    │   └── views/
    │       ├── base/
    │       │   ├── about.py
    │       │   ├── contact.py
    │       │   ├── home.py
    │       │   └── __init__.py
    │       ├── __init__.py
    │       └── user/
    │           ├── administration.py
    │           ├── edit.py
    │           ├── __init__.py
    │           ├── login.py
    │           ├── logout.py
    │           ├── members.py
    │           └── register.py
    ├── manage_commands/
    │   ├── create_database.py
    │   ├── create_data.py
    │   ├── create_superuser.py
    │   ├── drop_database.py
    │   ├── __init__.py
    │   ├── orm_test.py
    │   ├── run_coverage.py
    │   └── run_test.py
    └── manage.py

Copyright and licence
----------------------

|License: GPL v3| |License: Apache 2.0|

.. |License: GPL v3| image:: https://img.shields.io/badge/License-GPLv3-blue.svg
   :target: https://www.gnu.org/licenses/gpl-3.0

.. |License: Apache 2.0| image:: https://img.shields.io/badge/License-Apache%202.0-blue.svg
   :target: https://opensource.org/licenses/Apache-2.0

Copyright (C) 2017 by `vroncevic.github.io/flask_mod_struct <https://vroncevic.github.io/flask_mod_struct>`_

**flask_mod_struct** is free software; you can redistribute it and/or modify
it under the same terms as Python itself, either Python version 2.x/3.x or,
at your option, any later version of Python 3 you may have available.

Indices and tables
------------------

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
