"""
Main CLI
~~~~~~~~

Definition of {{ cookiecutter.project_name }} CLI.

"""

from pyapp.app import CliApplication, argument, CommandOptions


APP = CliApplication()
main = APP.dispatch


@APP.command
@argument("-n", "--name", default="Dave")
def hello(opts: CommandOptions):
    """
    Say hello
    """
    # Do command imports locally to improve startup time!
    print(f"Hello {opts.name}")


@APP.command(name="hello-async")
@argument("-n", "--name", default="Jane")
async def hello_async(opts: CommandOptions):
    """
    Say hello in an AsyncIO run-loop
    """
    # Do command imports locally to improve startup time!
    print(f"Hello {opts.name}")
