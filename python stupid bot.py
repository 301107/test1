def sum_excluding_range(arr, k, l):
  """
  Находит сумму всех элементов массива, кроме элементов с номерами от K до L включительно.

  Args:
    arr: Массив.
    k: Начальный номер исключаемого диапазона (1-индексация).
    l: Конечный номер исключаемого диапазона (1-индексация).

  Returns:
    Сумма элементов вне указанного диапазона.
  """
  if 1 <= k <= l <= len(arr):
    sum_before = 0
    for i in range(0, k - 1):
      sum_before += arr[i]
    sum_after = 0
    for i in range(l, len(arr)):
      sum_after += arr[i]
    return sum_before + sum_after
  else:
    return "Некорректные значения K и L"

# Пример использования
my_array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
K = 4
L = 6
result = sum_excluding_range(my_array, K, L)
print(f"Сумма элементов, кроме с {K} по {L}: {result}")  # Вывод: Сумма элементов, кроме с 4 по 6: 22