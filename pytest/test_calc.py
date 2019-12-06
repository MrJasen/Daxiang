import pytest


def add(x, y):
    return x + y


def test_add():
    assert add(1,2) == 3
    assert add(3,3) == 6
    assert add(4,4) == 8
