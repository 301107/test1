
def add(a, b):
    """Складывает два числа."""
    return a + b

def subtract(a, b):
    """Вычитает b из a."""
    return a - b

def multiply(a, b):
    """Умножает два числа."""
    return a * b

def divide(a, b):
    """Делит a на b. Возвращает ошибку, если b равно 0."""
    if b == 0:
        raise ValueError("Cannot divide by zero!")
    return a / b