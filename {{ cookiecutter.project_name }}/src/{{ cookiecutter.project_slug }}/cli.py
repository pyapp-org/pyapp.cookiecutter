"""
CLI
~~~

Definition of {{ cookiecutter.project_name }} CLI.

"""

from pyapp.app import CliApplication, argument, CommandOptions
from typing import Sequence

app = CliApplication()


@app.command
@argument("-n", "--name", default="Dave")
def hello(opts: CommandOptions):
    """
    Say hello
    """
    # Do command imports locally to improve startup time!

    print(f"Hello {opts.name}")


def main(args: Sequence[str] = None):
    """
    Main application entry point
    """
    app.dispatch(args)


if __name__ == "__main__":
    main()

