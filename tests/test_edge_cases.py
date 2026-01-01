import pytest

def divide(a, b):
    return a / b

def test_divide_by_zero():
    with pytest.raises(ZeroDivisionError):
        divide(1, 0)

def test_large_numbers():
    assert divide(1e100, 1e-100) == 1e200
