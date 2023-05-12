import pytest

from funcs import is_valid_die

def test_is_valid_die():
    assert is_valid_die('12345')
    assert not is_valid_die('abc')
    assert not is_valid_die(None)
    assert not is_valid_die(['A', 'B', 'C', 'D'])
    assert not is_valid_die(9876)
    assert not is_valid_die(123456789)

