from calculator import Calculator
import pytest

def test_sum():
    c1 = Calculator(10, 5)
    assert c1.sum() == 15
def test_subtract():
    c2 = Calculator(2, 2)
    assert c2.subtract() == 0
def test_multiply():
    c3 = Calculator(5, 5)
    assert c3.multiply() == 25
def test_divide():
    c4 = Calculator(20, 5)
    assert c4.divide() == 4
def test_divide_by_zero():
    c5 = Calculator(10, 0)
    assert c5.divide() is None
def test_sum_invalid_type():
    c6 = Calculator("abc", 5)
    with pytest.raises(TypeError):
        c6.sum()
def test_subtract_invalid_type():
    c7 = Calculator("abc", 5)
    with pytest.raises(TypeError):
        c7.subtract()
def test_multiply_invalid_type():
    c8 = Calculator("ddd", "hhh")
    with pytest.raises(TypeError):
        c8.multiply()
def test_divide_invalid_type():
    c9 = Calculator(7, "w")
    with pytest.raises(TypeError):
        c9.divide()