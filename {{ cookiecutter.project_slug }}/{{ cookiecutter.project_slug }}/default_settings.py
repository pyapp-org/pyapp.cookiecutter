# Enable "debug" mode
DEBUG = True

{% if cookiecutter.use_sqlalchemy %}
##############################################################################
# Database Engines

DATABASE_ENGINES = None

{% endif %}{% if cookiecutter.use_smtp %}
##############################################################################
# SMTP Host

SMTP = {
    "default": {
        "host": "hostname",
    },
}

{% endif %}
