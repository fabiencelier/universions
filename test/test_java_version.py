"""Test the Java version parser."""

from pathlib import Path

import pytest

from universions import Version
from universions.java import _parse_version_string, get_java_version

from .mock_popen import BasicMockedPopen

JAVA_5 = (
    b'java version "1.5.0_29"\n'
    b"Java(TM) 2 Runtime Environment, Standard Edition (build 1.5.0_29-b02)\n"
    b"Java HotSpot(TM) Server VM (build 1.5.0_29-b02, mixed mode)"
)

JAVA_6 = (
    b'openjdk version "1.6.0-119"\n'
    b"OpenJDK Runtime Environment (Zulu 6.22.0.3-linux64) (build 1.6.0-119-b119)\n"
    b"OpenJDK 64-Bit Server VM (Zulu 6.22.0.3-linux64) (build 23.77-b119, mixed mode)"
)

JAVA_7 = (
    b'java version "1.7.0_55"\n'
    b"Java(TM) SE Runtime Environment (build 1.7.0_55-b13)\n"
    b"Java HotSpot(TM) 64-Bit Server VM (build 24.55-b03, mixed mode)"
)

JAVA_8 = (
    b'java version "1.8.0_151"\n'
    b"Java(TM) SE Runtime Environment (build 1.8.0_151-b12)\n"
    b"Java HotSpot(TM) 64-Bit Server VM (build 25.151-b12, mixed mode)"
)

JAVA_11 = (
    b'openjdk version "11.0.5" 2019-10-15\n'
    b"OpenJDK Runtime Environment 18.9 (build 11.0.5+10)\n"
    b"OpenJDK 64-Bit Server VM 18.9 (build 11.0.5+10, mixed mode)"
)

JAVA_12 = (
    b'openjdk version "12.0.2" 2019-07-17\n'
    b"OpenJDK Runtime Environment (build 12.0.2+9-sapmachine)\n"
    b"OpenJDK 64-Bit Server VM (build 12.0.2+9-sapmachine, mixed mode, sharing)"
)

JAVA_13_J9 = (
    b'openjdk version "13.0.1" 2019-10-15\n'
    b"OpenJDK Runtime Environment AdoptOpenJDK (build 13.0.1+9)\n"
    b"Eclipse OpenJ9 VM AdoptOpenJDK (build openj9-0.17.0, JRE 13 Linux amd64-64-Bit "
    b"Compressed References 20191021_96 (JIT enabled, AOT enabled)\n"
    b"OpenJ9   - 77c1cf708\n"
    b"OMR      - 20db4fbc\n"
    b"JCL      - 74a8738189 based on jdk-13.0.1+9)\n"
)

JAVA_14_PRE = (
    b'openjdk version "14-ea" 2020-03-17\n'
    b"OpenJDK Runtime Environment (build 14-ea+20-879)\n"
    b"OpenJDK 64-Bit Server VM (build 14-ea+20-879, mixed mode, sharing)"
)

JAVA_PARAMETERS = [
    pytest.param(JAVA_5, "1.5.0_29", Version(1, 5, 29)),
    pytest.param(JAVA_6, "1.6.0_119", Version(1, 6, 119)),  # wrong parsing here
    pytest.param(JAVA_7, "1.7.0_55", Version(1, 7, 55)),
    pytest.param(JAVA_8, "1.8.0_151", Version(1, 8, 151)),
    pytest.param(JAVA_11, "11.0.5", Version(11, 0, 5)),
    pytest.param(JAVA_12, "12.0.2", Version(12, 0, 2)),
    pytest.param(JAVA_13_J9, "13.0.1", Version(13, 0, 1)),
    pytest.param(JAVA_14_PRE, "14-ea", Version(14, None, None, "ea", None)),
]

JAVA_HOME = Path.home() / "java"


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
