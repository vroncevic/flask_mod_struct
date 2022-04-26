Flask Module Structured Framework
----------------------------------

☯️ **flask_mod_struct** is framework for Flask web apps.

Developed in 🐍 `python <https://www.python.org/>`_ code.

The README is used to introduce the modules and provide instructions on
how to install the modules, any machine dependencies it may have and any
other information that should be provided before the modules are installed.

|python checker| |python package| |github issues| |documentation status| |github contributors|

.. |python checker| image:: https://img.shields.io/github/workflow/status/vroncevic/flask_mod_struct/flask_mod_struct_python_checker?style=flat&label=flask_mod_struct%20python%20checker
   :target: https://img.shields.io/github/workflow/status/vroncevic/flask_mod_struct/flask_mod_struct_python_checker

.. |python package| image:: https://img.shields.io/github/workflow/status/vroncevic/flask_mod_struct/flask_mod_struct_package_checker?style=flat&label=flask_mod_struct%20package%20checker
   :target: https://img.shields.io/github/workflow/status/vroncevic/flask_mod_struct/flask_mod_struct_package_checker

.. |github issues| image:: https://img.shields.io/github/issues/vroncevic/flask_mod_struct.svg
   :target: https://github.com/vroncevic/flask_mod_struct/issues

.. |github contributors| image:: https://img.shields.io/github/contributors/vroncevic/flask_mod_struct.svg
   :target: https://github.com/vroncevic/flask_mod_struct/graphs/contributors

.. |documentation status| image:: https://readthedocs.org/projects/flask-mod-struct/badge/?version=latest
   :target: https://flask-mod-struct.readthedocs.io/en/latest/?badge=latest

.. toctree::
   :maxdepth: 4
   :caption: Contents

   self

Installation
-------------

Navigate to release `page`_ download and extract release archive 📦.

.. _page: https://github.com/vroncevic/flask_mod_struct/releases

To install **flask_mod_struct** 📦 type the following

.. code-block:: bash

    tar xvzf flask_mod_struct-x.y.z.tar.gz
    cd flask_mod_struct-x.y.z/
    pip install -r requirements.txt
    cp manage.py /FlaskApp/
    cp -R /manage_commands/ /FlaskApp/
    cp -R /app_server/ /Flask/

You can use Docker to create image/container 🚢.

|github docker checker|

.. |github docker checker| image:: https://img.shields.io/github/workflow/status/vroncevic/flask_mod_struct/flask_mod_struct_docker_checker?style=flat&label=flask_mod_struct%20docker%20checker
   :target: https://img.shields.io/github/workflow/status/vroncevic/flask_mod_struct/flask_mod_struct_docker_checker

Dependencies
-------------

**flask_mod_struct** requires next modules and libraries

    alembic                           1.6.5
    Flask                             1.1.4
    Flask-Bcrypt                      1.0.1
    Flask-Bootstrap                   3.3.7.1
    Flask-Cors                        3.0.10
    Flask-DebugToolbar                0.13.1
    Flask-Login                       0.5.0
    Flask-Mail                        0.9.1
    Flask-Migrate                     2.6.0
    Flask-Script                      2.0.6
    Flask-SQLAlchemy                  2.5.1
    Flask-Testing                     0.8.1
    Flask-WTF                         0.14.3
    SQLAlchemy                        1.4.27
    Werkzeug                          1.0.1
    WTForms                           2.3.3

Library structure
------------------

**flask_mod_struct** is based on OOP

🧰 Framework structure

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
    │   └── __init__.py
    └── manage.py

Copyright and licence
----------------------

|license: gpl v3| |license: apache 2.0|

.. |license: gpl v3| image:: https://img.shields.io/badge/license-gplv3-blue.svg
   :target: https://www.gnu.org/licenses/gpl-3.0

.. |license: apache 2.0| image:: https://img.shields.io/badge/license-apache%202.0-blue.svg
   :target: https://opensource.org/licenses/apache-2.0

Copyright (C) 2017 by `vroncevic.github.io/flask_mod_struct <https://vroncevic.github.io/flask_mod_struct>`_

**flask_mod_struct** is free software; you can redistribute it and/or modify
it under the same terms as Python itself, either Python version 2.x/3.x or,
at your option, any later version of Python 3 you may have available.

🌎 🌍 🌏 Lets help and support PSF.

|python software foundation|

.. |python software foundation| image:: https://raw.githubusercontent.com/vroncevic/flask_mod_struct/dev/docs/psf-logo-alpha.png
   :target: https://www.python.org/psf/

|donate|

.. |donate| image:: https://www.paypalobjects.com/en_us/i/btn/btn_donatecc_lg.gif
   :target: https://psfmember.org/index.php?q=civicrm/contribute/transact&reset=1&id=2

Indices and tables
------------------

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
