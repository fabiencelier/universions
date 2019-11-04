"""Test the Git version parser."""

from universions.git import _extract_version

MAC_GIT = "git version 2.10.1 (Apple Git-78)"


def test_parse_classic_version():
    """Basic test."""
    parsed = _extract_version(MAC_GIT)
    assert parsed == "2.10.1"
