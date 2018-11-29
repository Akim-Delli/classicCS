import pytest

from boost2 import rollTheString


@pytest.mark.parametrize("word_input,rotation_input, expected_output", [
    ("abc", [3, 2, 1], "ddd"),
    ("aaa", [3, 2, 1], "dcb"),
    ("abc", [1, 1, 1], "dbc"),
    ("abz", [3], "bca"),
    ("vwxyz", [1, 2, 3, 4, 5], "aaaaa"),
    ("vgxgpuamkx", [5, 5, 2, 4, 7, 6, 2, 2, 8, 7], "fqenvydnkx"),
    ("aaaaaaaa", [1,1,1,1,1,1,1,1,1,1], "kaaaaaaa"),
])
def test_increment_integer_as_error(word_input, rotation_input, expected_output):
    assert rollTheString(word_input, rotation_input) == expected_output
