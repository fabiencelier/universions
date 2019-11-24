"""Test comparaison between versions."""

from universions import Version


def test_compare_version_to_tuple():
    """Compare a simple version to other numbers."""
    version = Version(2, 1)

    # EQ
    assert version == (2, 1)
    assert version == (2, 1, None)
    assert version == Version(2, 1)

    # LT
    assert version < (2, 2)
    assert version < (3, 0)
    assert version < (2, 1, 0)
    assert version < (3,)

    #  LTE
    assert version <= (2, 2)
    assert version <= (3, 0)
    assert version <= (2, 1)
    assert version <= (2, 1, 0)

    # GT
    assert version > (0, 1)
    assert version > (2, 0)
    assert version > (2,)

    # GTE
    assert version >= (0, 1)
    assert version >= (2, 0)
    assert version >= (2,)
    assert version >= (2, 1)

    # NE
    assert version != (2, 2)


def test_compare_partial():
    """Compare partial version numbers."""
    assert Version(1, 0) > Version(1)
    assert Version(1, 0, 0) > Version(1, 0)


def test_compare_prerelease():
    """Pre-release have a lower precedence than the associated normal version."""
    # https://semver.org/#spec-item-9
    assert Version(1, 0, 0) > Version(1, 0, 0, "beta")
    assert Version(1, 0, 0) > (1, 0, 0, "beta")
    assert Version(1, 0) > Version(1, 0, prerelease="beta")
    assert Version(1, 0) > (1, 0, None, "beta")

    assert Version(1, 0, 0, "beta") > Version(1, 0, 0, "alpha")
    assert Version(1, 0, 0, "alpha") < Version(1, 0, 0, "beta")
    assert Version(1, 0, 0, "alpha") == (1, 0, 0, "alpha")


def test_compare_build():
    """Build version must not be use in precedence."""
    # https://semver.org/#spec-item-10
    assert Version(1, 0, 0, None, "build1") == Version(1, 0, 0)
    assert Version(1, 0, 0, None, "build1") == Version(1, 0, 0, None, "build2")
