from pyapp.app import CliApplication, argument, CommandOptions
from typing import Sequence

import {{ cookiecutter.project_slug }}

app = CliApplication({{ cookiecutter.project_slug }})


@app.command
@argument("-n", "--name", default="Dave")
def hello(opts: CommandOptions):
    """
    Say hello
    """
    # Import an command requirements locally to improve load time!

    print(f"Hello {opts.name}")


def main(args: Sequence[str] = None):
    """
    Main application entry point
    """
    app.dispatch(args)


if __name__ == "__main__":
    main()
