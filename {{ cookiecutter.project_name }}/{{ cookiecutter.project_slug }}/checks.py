"""
Application Specific Checks
~~~~~~~~~~~~~~~~~~~~~~~~~~~
"""

from pyapp import checks
from pyapp.conf import Settings


@checks.register
def sample_check(settings: Settings, **_):
    # Return results of a check, normally a successful check returns nothing
    # but this is an example.
    return checks.Info("This is a sample message")
