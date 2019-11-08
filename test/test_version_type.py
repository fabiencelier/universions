"""Test the version type."""

from universions import Version


def test_define_basic_version():
    version = Version(1, 0, 2)
    assert version.major == 1
    assert version.minor == 0
    assert version.patch == 2
    assert version.prerelease is None
    assert version.build is None


def test_major_version():
    version = Version(10)
    assert version.major == 10
    assert version.minor is None
    assert version.patch is None
    assert version.prerelease is None
    assert version.build is None


def test_major_minor_version():
    version = Version(49, 52)
    assert version.major == 49
    assert version.minor == 52
    assert version.patch is None
    assert version.prerelease is None
    assert version.build is None


def test_full_version():
    version = Version(49, 52, 0, "rc.5", "eg5f6d")
    assert version.major == 49
    assert version.minor == 52
    assert version.patch == 0
    assert version.prerelease == "rc.5"
    assert version.build == "eg5f6d"


def test_compare_version_with_major_minor():
    version = Version(1, 0)
    assert version > (0, 1)
    assert version < (1, 1)
    #  assert version == (1, 0)
    assert version != (1, 0, 0)
    assert version < (2,)
    assert version > (0,)
    assert version > (0, 1, 10, "rc2", "build-455")
