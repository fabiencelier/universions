"""Test the version type."""

import unittest

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
    assert version.minor is 0
    assert version.patch is 0
    assert version.prerelease is None
    assert version.build is None


def test_major_minor_version():
    version = Version(49, 52)
    assert version.major == 49
    assert version.minor == 52
    assert version.patch is 0
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
    assert version > Version(0, 1)
    assert version < Version(1, 1)
    #  assert version == (1, 0)
    assert version != Version(1, 0, 0)
    assert version < Version(2)
    assert version > Version(0)
    assert version > Version(0, 1, 10, "rc2", "build-455")


def test_compare_version_to_prerelease():
    custom_build = Version(1, 0, 0, None, "dev20191101")
    early_access = Version(1, 0, 0, "rc1")
    release = Version(1, 0, 0)

    assert custom_build < early_access
    assert early_access < release
    # Ensure transitivity
    assert custom_build < release

    # And testing the opposite relation for the sake of completeness
    assert early_access > custom_build
    assert release > early_access
    assert release > custom_build


def create_values():
    for major in [1, 2]:
        for minor in [3, 4]:
            for patch in [5, 6]:
                for pre in ["7", "8"]:
                    for build in ["dev1", "dev10"]:
                        yield [major, minor, patch, pre, build]


def test_extensive_comparison_on_values():
    for te in create_values():
        entry = Version(*te)
        lower = True
        for tr in create_values():
            ref = Version(*tr)
            if te == tr:
                lower = False

                assert entry == ref
                assert ref == entry

                assert entry <= ref
                assert ref <= entry

                assert entry >= ref
                assert ref >= entry

                assert not (entry < ref)
                assert not (entry > ref)
                assert not (ref > entry)
                assert not (ref < entry)
                assert not (entry != ref)
                assert not (ref != entry)

            else:
                assert entry != ref
                assert ref != entry
                assert not (entry == ref)
                assert not (ref == entry)

                if lower:
                    assert entry > ref
                    assert entry >= ref
                    assert not (entry < ref)
                    assert not (entry <= ref)

                    assert ref < entry
                    assert ref <= entry
                    assert not (ref > entry)
                    assert not (ref >= entry)
                else:
                    assert entry < ref
                    assert entry <= ref
                    assert not (entry > ref)
                    assert not (entry >= ref)

                    assert ref > entry
                    assert ref >= entry
                    assert not (ref < entry)
                    assert not (ref <= entry)


def test_comparison_with_none_for_minor():
  assert Version(1, 1) > Version(1)
  assert Version(1, 1) > Version(1)
  assert Version(1, 1) > Version(1)
  assert Version(1, 1) < Version(2)
  assert Version(1, 1) < Version(2, None, None, "ea")
  assert Version(1, 1) < Version(2, None, None, None, "dev2019")


def test_comparison_with_none_for_patch():
  assert Version(1, 2, 3) > Version(1, 2)
  assert Version(1, 2, 3) < Version(1, 3)


def test_comparison_tail():
  assert Version(1, 2, 3) > Version(1, 2, 3, "4")
  assert Version(1, 2, 3, None, "dev1") < Version(1, 2, 3)
  assert Version(1, 2, 3, None, "dev10") < Version(1, 2, 3, "ea", "dev1")
