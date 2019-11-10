"""Test the Python version."""
from pathlib import Path

import pytest

from universions import Version
from universions.python import get_python_version

from .mock_popen import BasicMockedPopen

PY_2_5_1 = b"Python 2.5.1"
PY_2_7_17 = b"Python 2.7.17rc1"
PY_3_0 = b"Python 3.0"
PY_3_6_9 = b"Python 3.6.9"
PY_3_7_5 = b"Python 3.7.5rc1"
PY_3_8_0 = b"Python 3.8.0b2+"
PY_3_9_DEV = b"Python 3.9.0a0"

PYPY_3_6_9 = (
    b"Python 3.6.9 (5da45ced70e515f94686be0df47c59abd1348ebc, Oct 17 2019, 22:59:56)\n"
    b"[PyPy 7.2.0 with GCC 8.2.0]"
)

JYTHON = b"Jython 2.5.4rc1"

VERSIONS = [
    pytest.param(PY_2_5_1, Version(2, 5, 1)),
    pytest.param(PY_2_7_17, Version(2, 7, 17, "rc1")),
    pytest.param(PY_3_0, Version(3, 0, 0)),
    pytest.param(PY_3_6_9, Version(3, 6, 9)),
    pytest.param(PY_3_7_5, Version(3, 7, 5, "rc1")),
    pytest.param(PY_3_8_0, Version(3, 8, 0, "b2+")),
    pytest.param(PY_3_9_DEV, Version(3, 9, 0, "a0")),
    pytest.param(PYPY_3_6_9, Version(3, 6, 9)),
    pytest.param(JYTHON, Version(2, 5, 4, "rc1")),
]


class TestPython(BasicMockedPopen):
    """Test the Python version."""

    @pytest.mark.parametrize("command,version", VERSIONS)
    def test_default_python_version(self, command: bytes, version: Version):
        """Test that the correct version is returned."""
        self.popen.set_command("python --version", stderr=command)
        assert get_python_version() == version

    @pytest.mark.parametrize("command,version", VERSIONS)
    def test_python_version_with_path(self, command: bytes, version: Version):
        """Test that the correct version is returned."""
        path = str(Path.home() / "python" / "bin" / "python")
        self.popen.set_command(f"{path} --version", stderr=command)
        assert get_python_version(path=path) == version
