"""Module for Pip version.

Seems that pip version isreally similar to python :
  - "pip 19.3.1 from /path/python3.7/site-packages/pip (python 3.7)"
  - "pip 10.0.0b2 from /path/lib/python2.7/site-packages/pip (python 2.7)"
  - "pip 18 .1 from /path/lib/python3.6/site-packages/pip (python 3.6)"

"""

from pathlib import Path
from typing import Optional, Union

from .._exec import exec_command
from ..python._parser import parse_python_version
from ..version import Version


def get_pip_version(path: Optional[Union[Path, str]] = None) -> Optional[Version]:
    """Get the Pip version.

    Args:
        path: The path to the Pip to check. If not defined, it uses "pip"
    Returns:
        The Pip version.

    """
    if path is None:
        path = "pip"
    version_string = exec_command([path, "--version"], use_stderr=True)
    version = version_string.split(" ")[1]
    return parse_python_version(version)
