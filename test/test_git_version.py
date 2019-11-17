"""Test the Git version parser."""

from pathlib import Path

import pytest

from universions import Version
from universions.git import _extract_version

from .mock_popen import BasicMockedPopen

MAC_GIT = "git version 2.10.1 (Apple Git-78)"
UNIX_GIT = "git version 2.23.0"
OLD_GIT = "git version 1.7.7.3"
WINDOWS_GIT = "git version 2.24.0.windows.1"
CYGWIN_GIT = "git version 1.9.5.msysgit.0"


class TestJava(BasicMockedPopen):
    """Test the Java version"""

    @pytest.fixture()
    def clear_java_home(self, monkeypatch):
        """Clear the JAVA_HOME environment variable."""
        monkeypatch.delenv("JAVA_HOME")

    @pytest.fixture()
    def set_java_home(self, monkeypatch):
        """Set the JAVA_HOME environment variable."""
        monkeypatch.setenv("JAVA_HOME", str(JAVA_HOME))

    @pytest.mark.usefixtures(clear_java_home.__name__)
    @pytest.mark.parametrize("command,string,version", JAVA_PARAMETERS)
    def test_java_version_without_java_home(
        self, command: bytes, string: str, version: Version
    ):
        """Test that the correct version is returned."""
        self.popen.set_command("java -version", stderr=command)
        assert get_java_version() == version
        assert string == _parse_version_string(str(command, encoding="utf8"))

    @pytest.mark.usefixtures(set_java_home.__name__)
    @pytest.mark.parametrize("command,string,version", JAVA_PARAMETERS)
    def test_java_version_with_java_home(
        self, command: bytes, string: str, version: Version
    ):
        """Test the java version from JAVA_HOME"""
        java_path = str(JAVA_HOME / "bin" / "java")
        self.popen.set_command(f"{java_path} -version", stderr=command)
        assert get_java_version() == version

    @pytest.mark.usefixtures(clear_java_home.__name__)
    @pytest.mark.parametrize("command,string,version", JAVA_PARAMETERS)
    def test_java_version_with_java_path(
        self, command: bytes, string: str, version: Version
    ):
        """Test that the correct version is returned."""
        java_path = str(Path.home() / "my_java" / "bin" / "java")
        self.popen.set_command(f"{java_path} -version", stderr=command)
        assert get_java_version(java_path=java_path) == version

def test_parse_mac_version():
    """Tests with the output of Mac OS."""
    parsed = _extract_version(MAC_GIT)
    assert parsed == "2.10.1"


def test_parse_unix_version():
    """Tests with the output of a standard unix."""
    parsed = _extract_version(UNIX_GIT)
    assert parsed == "2.23.0"


def test_old_version():
    """Tests parsing of an old git version."""
    parsed = _extract_version(OLD_GIT)
    assert parsed == "1.7.7.3"


def test_windows_version():
    """Tests parsing of git for Windows."""
    parsed = _extract_version(WINDOWS_GIT)
    assert parsed == "2.24.0.windows.1"


def test_cygwin_version():
    """Tests parsing of git for Cygwin."""
    parsed = _extract_version(CYGWIN_GIT)
    assert parsed == "1.9.5.msysgit.0"
