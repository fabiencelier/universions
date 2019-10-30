"""Test the version type."""

from universions import Version

def test_define_basic_version():
    version = Version(1,0,2)
    print(version)
    assert version.major == 1
    assert version.minor == 0
    assert version.micro == 2
    assert version.releaselevel == None
    assert version.serial == None