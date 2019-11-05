"""Test the Git version parser."""

from universions.git import _extract_version

MAC_GIT = "git version 2.10.1 (Apple Git-78)"

UNIX_GIT = "git version 2.23.0"


def test_parse_mac_version():
    """Basic test."""
    parsed = _extract_version(MAC_GIT)
    assert parsed == "2.10.1"


def test_parse_unix_version():
    """Basic test."""
    parsed = _extract_version(UNIX_GIT)
    assert parsed == "2.23.0"
