import pytest
from your_module import ekub

def test_ekub():
    assert ekub(12, 15) == 3
    assert ekub(24, 30) == 6
    assert ekub(7, 5) == 1
    assert ekub(48, 18) == 6
    assert ekub(101, 103) == 1

def test_ekub_zero():
    with pytest.raises(ZeroDivisionError):
        ekub(0, 10)
    with pytest.raises(ZeroDivisionError):
        ekub(10, 0)

def test_ekub_negative():
    assert ekub(-12, 15) == 3
    assert ekub(24, -30) == 6
    assert ekub(-7, -5) == 1

def test_ekub_equal():
    assert ekub(10, 10) == 10
    assert ekub(20, 20) == 20
