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

    if "Not open source" == "{{ cookiecutter.open_source_license }}":
        remove_file("LICENSE")
