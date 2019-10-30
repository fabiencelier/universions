"""Test the semver parser."""

from universions import parse_semver, Version


def test_full_01():
    """Test parsefull version."""
    expected = {
        "1.0.0": Version(1, 0, 0),
        "1.2.3-alpha.1.2+build.11.e0f985a": Version(
            1, 2, 3, "alpha.1.2", "build.11.e0f985a"
        ),
        "3.4.5-pre.2+build.4": Version(3, 4, 5, "pre.2", "build.4"),
    }
    for (string, version) in expected.items():
        assert parse_semver(string) == version
