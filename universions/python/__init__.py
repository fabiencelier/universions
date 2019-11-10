"""Module for Python version.

The version comes from the Python in command line and not the one running the script.

Python version can be get by calling ``python --version`` or ``python -V`

The returned value is "Python" followed by the version number :
    - "Python 2.5.1"
    - "Python 3.6.9"
Possible variations :
    - incomplete number : "Python 3.0"
    - prerelease number :
        - "Python 3.7.5rc1"
        - "Python 3.8.0b2+"
        - "Python 3.9.0a0"
    - Jython : "Jython 2.5.4rc1"
    - Multiline :
        "Python 3.6.9 (5da45ced70e515f94686be0df47c59abd1348ebc, Oct 17 2019, 22:59:56)"
        "[PyPy 7.2.0 with GCC 8.2.0]"

It is not a valid semver number as the prerelease value does not start with "-"

"""

from pathlib import Path
from typing import Optional, Union

from .._exec import exec_command
from ..version import Version
from ._parser import parse_python_version


def get_python_version(path: Optional[Union[Path, str]] = None) -> Optional[Version]:
    """Get the Python version.

    Args:
        path: The path to the Python to check. If not defined, it uses "python"
    Returns:
        The Python version.

    """
    if path is None:
        path = "python"
    version_string = exec_command([path, "--version"], use_stderr=True)
    version = version_string.split(" ")[1]

    return parse_python_version(version)
