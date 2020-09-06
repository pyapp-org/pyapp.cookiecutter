#!/usr/bin/env python3
from pathlib import Path

PROJECT_DIR = Path().resolve()


def remove_file(file_path: str):
    (PROJECT_DIR / file_path).unlink()


if __name__ == "__main__":
    if "{{ cookiecutter.use_pytest }}" == "y":
        remove_file("tests/__init__.py")
    else:
        remove_file("tests/conftest.py")

    # Remove licence file for proprietary applications
    if "Not open source" == "{{ cookiecutter.open_source_license }}":
        remove_file("LICENSE")

    # Remove other dependency tools
    dependency_tool = "{{ cookiecutter.dependency_tool }}".lower()
    if dependency_tool == "pipenv":
        remove_file("pyproject.toml")
        remove_file("requirements.txt")

    elif dependency_tool == "poetry":
        remove_file("Pipfile")
        remove_file("requirements.txt")

    else:  # requirements.txt
        remove_file("Pipfile")
        remove_file("pyproject.toml")
