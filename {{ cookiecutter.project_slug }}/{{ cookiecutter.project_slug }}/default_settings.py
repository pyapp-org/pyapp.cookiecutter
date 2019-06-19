# Enable "debug" mode
DEBUG = True

{% if cookiecutter.use_sqlalchemy %}
DATABASE_ENGINES = None
{% endif %}{% if cookiecutter.use_smtp %}
SMTP = {
    "default": {
        "host": "hostname",
    },
}
{% endif %}
