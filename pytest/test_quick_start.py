import pytest
def reverse(string):
    return string[::-1]

def test_reverse():
    string = 'good'
    assert reverse(string) == 'doog'

    another_string='itest'
    assert  reverse(another_string)=='tseti'

def test_zero_division():
    with pytest.raises(ZeroDivisionError):
        1/0