import re
import sys


PACKAGE_REGEX = r"^[_a-zA-Z][\-_a-zA-Z0-9]+$"
MODULE_REGEX = r"^[_a-zA-Z][_a-zA-Z0-9]+$"


package_name = "{{ cookiecutter.package_name }}"
module_name = "{{ cookiecutter.app_name }}"


if not re.match(PACKAGE_REGEX, package_name):
    msg = (
        "ERROR: The package name '{}' is not a valid Python package name."
    )
    print(msg.format(module_name))

    # Exit to cancel project creation
    sys.exit(1)


if not re.match(MODULE_REGEX, module_name):
    msg = (
        "ERROR: The module name '{}' is not a valid Python module name. "
        "Please do not use a '-' character and use '_' instead."
    )
    print(msg.format(module_name))

    # Exit to cancel project creation
    sys.exit(1)
