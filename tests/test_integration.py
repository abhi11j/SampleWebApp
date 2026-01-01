import pytest

def multiply(a, b):
    return a * b

def add(a, b):
    return a + b

def test_add_then_multiply():
    result = multiply(add(2, 3), 4)
    assert result == 20
