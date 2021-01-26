"""
5. В массиве найти максимальный отрицательный элемент. Вывести на экран его значение и позицию в массиве.
Примечание к задаче: пожалуйста не путайте «минимальный» и «максимальный отрицательный». Это два абсолютно разных значения.
"""

from random import randint


numbers = [randint(-32, 32) for _ in range(32)]
print(numbers)

max_index = None
for index, value in enumerate(numbers):
    if max_index is not None and 0 > value > numbers[max_index]:
        max_index = index
    elif max_index is None and value < 0:
        max_index = index

if max_index is not None:
    print(f'Max negative number has position "{max_index}" and value "{numbers[max_index]}"')
else:
    print(f'Element not fount!')
