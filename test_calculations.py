
from my_calculations import add, subtract, multiply, divide

def test_add_positive_numbers():
    """Тест сложения двух положительных чисел."""
    assert add(2, 3) == 5

def test_add_negative_numbers():
    """Тест сложения двух отрицательных чисел."""
    assert add(-1, -5) == -6

def test_add_zero():
    """Тест сложения с нулем."""
    assert add(10, 0) == 10

def test_subtract_positive():
    """Тест вычитания положительных чисел."""
    assert subtract(5, 2) == 3

def test_subtract_negative_result():
    """Тест вычитания с отрицательным результатом."""
    assert subtract(2, 5) == -3

def test_multiply_simple():
    """Тест простого умножения."""
    assert multiply(4, 5) == 20

def test_multiply_by_zero():
    """Тест умножения на ноль."""
    assert multiply(7, 0) == 0

def test_divide_simple():
    """Тест простого деления."""
    assert divide(10, 2) == 5.0 # Результат деления в Python всегда float

def test_divide_by_one():
    """Тест деления на единицу."""
    assert divide(100, 1) == 100.0

# Импортируем pytest для специальных случаев тестирования исключений
import pytest

def test_divide_by_zero_raises_error():
    """Тест деления на ноль, ожидаем ошибку ValueError."""
    with pytest.raises(ValueError, match="Cannot divide by zero!"):
        divide(10, 0)