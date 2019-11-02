"""Test the Java version parser."""

from universions import Version
from universions.java import _parse_version_string, _parse_version

JAVA_8 = (
    'java version "1.8.0_151"\n'
    "Java(TM) SE Runtime Environment (build 1.8.0_151-b12)\n"
    "Java HotSpot(TM) 64-Bit Server VM (build 25.151-b12, mixed mode)"
)


def test_parse_classic_version():
    """Basic test."""
    parsed = _parse_version_string(JAVA_8)
    assert parsed == "1.8.0_151"
    version = _parse_version(parsed)
    assert version == Version(1, 8, 151)
