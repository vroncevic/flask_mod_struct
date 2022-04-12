<img align="right" src="https://raw.githubusercontent.com/vroncevic/flask_mod_struct/master/docs/flask_mod_struct_logo.png" width="25%">

# Flask Module Structured Framework

☯️ **flask_mod_struct** is framework for managing Flask App.

Developed in 🐍 **[python](https://www.python.org/)** code.

The README is used to introduce the modules and provide instructions on
how to install the modules, any machine dependencies it may have and any
other information that should be provided before the modules are installed.

[![flask_mod_struct py checker](https://github.com/vroncevic/flask_mod_struct/actions/workflows/flask_mod_struct_py_checker.yml/badge.svg)](https://github.com/vroncevic/flask_mod_struct/actions/workflows/flask_mod_struct_py_checker.yml) [![flask_mod_struct python package](https://github.com/vroncevic/flask_mod_struct/actions/workflows/flask_mod_struct_package.yml/badge.svg)](https://github.com/vroncevic/flask_mod_struct/actions/workflows/flask_mod_struct_package.yml) [![GitHub issues open](https://img.shields.io/github/issues/vroncevic/flask_mod_struct.svg)](https://github.com/vroncevic/flask_mod_struct/issues) [![GitHub contributors](https://img.shields.io/github/contributors/vroncevic/flask_mod_struct.svg)](https://github.com/vroncevic/flask_mod_struct/graphs/contributors)

<!-- START doctoc generated TOC please keep comment here to allow auto update -->
<!-- DON'T EDIT THIS SECTION, INSTEAD RE-RUN doctoc TO UPDATE -->
**Table of Contents**

- [Installation](#installation)
- [Usage](#usage)
- [Dependencies](#dependencies)
- [Package structure](#package-structure)
- [Docs](#docs)
- [Contributing](#contributing)
- [Copyright and licence](#copyright-and-licence)

<!-- END doctoc generated TOC please keep comment here to allow auto update -->

### Installation

Navigate to **[release page](https://github.com/vroncevic/flask_mod_struct/releases)** download and extract release archive 📦.

To install modules type the following

```bash
tar xvzf flask_mod_struct-x.y.z.tar.gz
cd flask_mod_struct-x.y.z/
pip install -r requirements.txt
cp manage.py /FlaskApp/
cp -R /manage_commands/ /FlaskApp/
cp -R /app_server/ /Flask/
```

Or You can use Dockerfile to create image/container 🚢.

[![flask_mod_struct docker checker](https://github.com/vroncevic/flask_mod_struct/actions/workflows/flask_mod_struct_docker_checker.yml/badge.svg)](https://github.com/vroncevic/flask_mod_struct/actions/workflows/flask_mod_struct_docker_checker.yml)

### Usage

Create databse

```bash
$ python manage.py create_db
Create database/tables
Done
```

Init databse and prepare alembic table

```bash
$ python manage.py db init
  Creating directory /data/dev/python/flask_mod_struct/github/flask_mod_struct/migrations ...  done
  Creating directory /data/dev/python/flask_mod_struct/github/flask_mod_struct/migrations/versions ...  done
  Generating /data/dev/python/flask_mod_struct/github/flask_mod_struct/migrations/env.pyc ...  done
  Generating /data/dev/python/flask_mod_struct/github/flask_mod_struct/migrations/env.py ...  done
  Generating /data/dev/python/flask_mod_struct/github/flask_mod_struct/migrations/alembic.ini ...  done
  Generating /data/dev/python/flask_mod_struct/github/flask_mod_struct/migrations/README ...  done
  Generating /data/dev/python/flask_mod_struct/github/flask_mod_struct/migrations/script.py.mako ...  done
  Please edit configuration/connection/logging settings in
  '/data/dev/python/flask_mod_struct/github/flask_mod_struct/migrations/alembic.ini' before proceeding.
```

Generate a migration script that makes the database match the models

```bash
$ python manage.py db migrate
INFO  [alembic.runtime.migration] Context impl SQLiteImpl.
INFO  [alembic.runtime.migration] Will assume non-transactional DDL.
INFO  [alembic.env] No changes in schema detected.
```

Create super user

```bash
$ python manage.py createsuperuser
Creating superuser account
Insert username of superuser: adroot
Insert email of superuser: adroot@test.com
Insert password of superuser: 
Done
```

Run application

```bash
$ python manage.py runserver
 * Serving Flask app "app_server" (lazy loading)
 * Environment: production
   WARNING: This is a development server. Do not use it in a production deployment.
   Use a production WSGI server instead.
 * Debug mode: on
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
 * Restarting with stat
 * Debugger is active!
 * Debugger PIN: 226-526-932
```

### Dependencies

**flask_mod_struct** requires other modules and libraries (Python 2.x)

```bash
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
```

### Package structure

🧰 Expected framework structure

```bash
app_server/
├── configuration/
│   ├── database/
│   │   ├── development_config.py
│   │   ├── __init__.py
│   │   ├── production_config.py
│   │   └── test_config.py
│   ├── development_config.py
│   ├── __init__.py
│   ├── mail/
│   │   ├── development_config.py
│   │   ├── __init__.py
│   │   ├── production_config.py
│   │   └── test_config.py
│   ├── production_config.py
│   └── test_config.py
├── forms/
│   ├── base/
│   │   ├── contact.py
│   │   └── __init__.py
│   ├── __init__.py
│   └── user/
│       ├── edit.py
│       ├── __init__.py
│       ├── login.py
│       └── register.py
├── __init__.py
├── models/
│   ├── __init__.py
│   └── model_user.py
├── static/
│   ├── base.css
│   └── favicon.ico
├── templates/
│   ├── base/
│   │   ├── about.html
│   │   ├── contact.html
│   │   └── home.html
│   ├── _base.html
│   ├── errors/
│   │   ├── 401.html
│   │   ├── 403.html
│   │   ├── 404.html
│   │   └── 500.html
│   ├── footer.html
│   ├── header.html
│   └── user/
│       ├── administration.html
│       ├── edit.html
│       ├── login.html
│       ├── members.html
│       └── register.html
└── views/
    ├── base/
    │   ├── about.py
    │   ├── contact.py
    │   ├── home.py
    │   └── __init__.py
    ├── __init__.py
    └── user/
        ├── administration.py
        ├── edit.py
        ├── __init__.py
        ├── login.py
        ├── logout.py
        ├── members.py
        └── register.py
```

### Docs

[![Documentation Status](https://readthedocs.org/projects/flask-mod-struct/badge/?version=latest)](https://flask-mod-struct.readthedocs.io/en/latest/?badge=latest) [![pages-build-deployment](https://github.com/vroncevic/flask_mod_struct/actions/workflows/pages/pages-build-deployment/badge.svg)](https://github.com/vroncevic/flask_mod_struct/actions/workflows/pages/pages-build-deployment)

📗 More documentation and info at

- [flask_mod_struct.readthedocs.io](https://flask_mod_struct.readthedocs.io/en/latest/)
- [www.python.org](https://www.python.org/)

### Contributing

[Contributing to flask_mod_struct](CONTRIBUTING.md)

### Copyright and licence

[![License: GPL v3](https://img.shields.io/badge/License-GPLv3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0) [![License](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)

Copyright (C) 2017 by [vroncevic.github.io/flask_mod_struct](https://vroncevic.github.io/flask_mod_struct/)

**flask_mod_struct** is free software; you can redistribute it and/or modify
it under the same terms as Python itself, either Python version 2.x or,
at your option, any later version of Python 2 you may have available.

Lets help and support PSF.

[![Python Software Foundation](https://raw.githubusercontent.com/vroncevic/flask_mod_struct/dev/docs/psf-logo-alpha.png)](https://www.python.org/psf/)

[![Donate](https://www.paypalobjects.com/en_US/i/btn/btn_donateCC_LG.gif)](https://psfmember.org/index.php?q=civicrm/contribute/transact&reset=1&id=2)
