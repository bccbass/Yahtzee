import pytest

from funcs import is_valid_die, input_filter

def test_is_valid_die():
    assert is_valid_die('12345')
    assert not is_valid_die('abc')
    assert not is_valid_die(None)
    assert not is_valid_die(['A', 'B', 'C', 'D'])
    assert not is_valid_die(9876)
    assert not is_valid_die(123456789)

def test_input_filter():
    assert input_filter('RESET') == 'r'
    assert input_filter('reset') == False
    assert not input_filter('RESET') == False
    assert input_filter('h') == 'h'
    assert input_filter('help') == 'h'
    assert not input_filter('h') == False
    assert input_filter('q') == 'q'
    assert input_filter('quit') == 'q'
    assert not input_filter('q') == False
    assert input_filter('wrong input') == False
    
    
    assert not input_filter('rffasldkf')
