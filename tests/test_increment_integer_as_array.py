import pytest

from increment_integer_as_array import increment_integer_as_array


@pytest.mark.parametrize("test_input,expected_output", [
    ([1, 2, 9], [1, 3, 0]),
    ([5], [6]),
    ([9, 9, 9, 9], [1, 0, 0, 0, 0]),
])
def test_increment_integer_as_error(test_input, expected_output):
    assert increment_integer_as_array(test_input) == expected_output
