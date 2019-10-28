from universions.java import _parse_version_string

java8 = (
    'java version "1.8.0_151"\n'
    "Java(TM) SE Runtime Environment (build 1.8.0_151-b12)\n"
    "Java HotSpot(TM) 64-Bit Server VM (build 25.151-b12, mixed mode)"
)


def test_simple_simple_parse():
    parsed = _parse_version_string(java8)
    assert parsed == "1.8.0_151"
