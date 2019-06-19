from pyapp.app import CliApplication, argument

import {{ cookiecutter.project_slug }}

app = CliApplication({{ cookiecutter.project_slug }})


@app.command
@argument("-n", "--name", default="Dave")
def hello(opts):
    """
    Say hello
    """
    print(f"Hello {opts.name}")


def main(args=None):
    app.dispatch(args)


if __name__ == "__main__":
    main()
