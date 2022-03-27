<img align="right" src="https://raw.githubusercontent.com/vroncevic/flask_mod_struct/dev/docs/flask_mod_struct_logo.png" width="25%">

# Flask Module Structured Framework

**flask_mod_struct** is framework for managing Flask App.

Developed in **[python](https://www.python.org/)** code.

The README is used to introduce the modules and provide instructions on
how to install the modules, any machine dependencies it may have and any
other information that should be provided before the modules are installed.

![Python package](https://github.com/vroncevic/flask_mod_struct/workflows/Python%20package%20flask_mod_struct/badge.svg?branch=master) [![GitHub issues open](https://img.shields.io/github/issues/vroncevic/flask_mod_struct.svg)](https://github.com/vroncevic/flask_mod_struct/issues) [![GitHub contributors](https://img.shields.io/github/contributors/vroncevic/flask_mod_struct.svg)](https://github.com/vroncevic/flask_mod_struct/graphs/contributors)

<!-- START doctoc generated TOC please keep comment here to allow auto update -->
<!-- DON'T EDIT THIS SECTION, INSTEAD RE-RUN doctoc TO UPDATE -->

**Table of Contents**

- [Installation](#installation)
- [Dependencies](#dependencies)
- [Package structure](#package-structure)
- [Docs](#docs)
- [Contributing](#contributing)
- [Copyright and licence](#copyright-and-licence)

<!-- END doctoc generated TOC please keep comment here to allow auto update -->

### Installation

Navigate to **[release page](https://github.com/vroncevic/flask_mod_struct/releases)** download and extract release archive.

To install modules type the following

```bash
tar xvzf flask_mod_struct-x.y.z.tar.gz
cd flask_mod_struct-x.y.z/
pip install -r requirements.txt
cp manage.py /FlaskApp/
cp -R /manage_commands/ /FlaskApp/
cp -R /app_server/ /Flask/
```

Or You can use docker to create image/container.

[![flask_mod_struct docker checker](https://github.com/vroncevic/flask_mod_struct/workflows/flask_mod_struct%20docker%20checker/badge.svg)](https://github.com/vroncevic/flask_mod_struct/actions?query=workflow%3A%22flask_mod_struct+docker+checker%22)

### Dependencies

**flask_mod_struct** requires other modules and libraries (Python 2.x/3.x)

```bash
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
```

### Package structure

Expected framework structure

```bash
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
```

### Docs

[![Documentation Status](https://readthedocs.org/projects/flask_mod_struct/badge/?version=latest)](https://flask_mod_struct.readthedocs.io/projects/flask_mod_struct/en/latest/?badge=latest)

- [flask_mod_struct.readthedocs.io](https://flask_mod_struct.readthedocs.io/en/latest/)
- [www.python.org](https://www.python.org/)

### Contributing

[Contributing to config_flask](CONTRIBUTING.md)

### Copyright and licence

[![License: GPL v3](https://img.shields.io/badge/License-GPLv3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0) [![License](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)

Copyright (C) 2017 by [vroncevic.github.io/flask_mod_struct](https://vroncevic.github.io/flask_mod_struct/)

**flask_mod_struct** is free software; you can redistribute it and/or modify
it under the same terms as Python itself, either Python version 2.x/3.x or,
at your option, any later version of Python 3 you may have available.

Lets help and support PSF.

[![Python Software Foundation](https://raw.githubusercontent.com/vroncevic/flask_mod_struct/dev/docs/psf-logo-alpha.png)](https://www.python.org/psf/)

[![Donate](https://www.paypalobjects.com/en_US/i/btn/btn_donateCC_LG.gif)](https://psfmember.org/index.php?q=civicrm/contribute/transact&reset=1&id=2)
