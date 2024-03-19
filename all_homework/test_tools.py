from tools import calculator
import pytest


@pytest.fixture()
def calc():
    return calculator(10, 5)

def test_add(calc):
    assert calc.add() == 15

def test_subtract(calc):
    assert calc.subtract() == 5

def test_multiply(calc):
    assert calc.multiply() == 50

def test_divide(calc):
    assert calc.divide() == 2

def test_div_by_zero():
    with pytest.raises(ZeroDivisionError):
        calculator(10, 0).divide()