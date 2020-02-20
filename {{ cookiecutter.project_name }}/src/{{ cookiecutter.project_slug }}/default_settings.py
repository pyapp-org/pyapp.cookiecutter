"""
Default Settings
~~~~~~~~~~~~~~~~

Use this file to define all of your applications settings. These settings can be
overridden by run-time settings.

"""
# Enable "debug" mode
DEBUG = True

{% if cookiecutter.use_sqlalchemy == "y" %}
##############################################################################
# Database Engines

DATABASE_ENGINES = None
"""
SQLAlchemy engine connection settings

Example settings::

    DATABASE_ENGINES = {
        "default": {
            "url": "driver://user:password@host/database",
            "connect_args": {
                # Engine specific args
            }
        }
    }

"""


{% endif %}{% if cookiecutter.use_smtp == "y" %}
##############################################################################
# SMTP Host

SMTP = {"default": {"host": "localhost"}}
"""
SMTP server settings

Example settings::

    SMTP = {
        "default": {
            "host": "localhost",
            "port": 23,
            "username": None,
            "password": None,
        },
    }
"""

{% endif %}