from calculator.calculator import Calculator
import pytest


@pytest.fixture
def calculator():
    return Calculator()

def test_initial_value(calculator):
    assert calculator.value == 0

def test_add(calculator):
    assert calculator.add(5) == 5
    assert calculator.add(2.5) == 7.5

def test_subtract(calculator):
    assert calculator.subtract(3) == -3
    assert calculator.subtract(2.5) == -5.5

def test_multiply(calculator):
    calculator.add(3)
    assert calculator.multiply(4) == 12
    assert calculator.multiply(0.5) == 6

def test_divide(calculator):
    calculator.add(10)
    assert calculator.divide(2) == 5
    assert calculator.divide(0.5) == 10
    with pytest.raises(ValueError):
        calculator.divide(0)

def test_take_root(calculator):
    calculator.reset_memory()
    calculator.add(16)
    assert calculator.take_root(2) == 4


def test_reset_memory(calculator):
    calculator.add(10)
    calculator.reset_memory()
    assert calculator.value == 0
