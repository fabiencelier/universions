"""Test the semver parser."""

import pytest

from universions import Version, parse_semver
from universions.error import InvalidVersionFormatError


@pytest.mark.parametrize(
    "version, expected",
    [
        ("1.0.0", Version(1, 0, 0)),
        (
            "1.2.3-alpha.1.2+build.11.e0f985a",
            Version(1, 2, 3, "alpha.1.2", "build.11.e0f985a"),
        ),
        ("3.4.5-pre.2+build.4", Version(3, 4, 5, "pre.2", "build.4")),
    ],
)
def test_default_semver_parser(version, expected):
    """Test parsefull version."""
    assert parse_semver(version) == expected


@pytest.mark.parametrize("version", ["1", "1.2", "v1.0.0"])
def test_default_semver_parser_failing_cases(version):
    """Test default sermver parser fails for invalid version."""
    with pytest.raises(InvalidVersionFormatError):
        parse_semver(version)


@pytest.mark.parametrize(
    "version, expected",
    [
        ("v1.0.0", Version(1, 0, 0)),
        ("V2.2.2", Version(2, 2, 2)),
        ("3.10.5", Version(3, 10, 5)),
    ],
)
def test_semver_parser_remove_initial_v(version: str, expected: Version):
    """Test the option to remove initial v"""
    assert parse_semver(version, remove_initial_v=True) == expected


@pytest.mark.parametrize("version", ["vv1.0.0", "v", "Vv3", "version1.0.0", "v-2.5.2"])
def test_semver_parser_invalid_initial_v(version: str):
    """Test the option to remove initial v when the string is invalid"""
    with pytest.raises(InvalidVersionFormatError):
        parse_semver(version, remove_initial_v=True)
