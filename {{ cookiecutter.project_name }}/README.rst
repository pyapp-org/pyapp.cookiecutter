{{ '#' * cookiecutter.project_name|length }}
{{ cookiecutter.project_name }}
{{ '#' * cookiecutter.project_name|length }}

Welcome to your pyApp project!

Getting Started
===============

Install required dependencies with ``pipenv install``.

Application is ready to execute from the `src` folder. Use 
``pipenv run python -m {{ cookiecutter.project_slug }}`` to use the CLI.

