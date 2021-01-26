"""
3. В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.
"""

from random import randint


numbers = [randint(0, 100) for _ in range(16)]
print(numbers)

min_index, max_index = 0, 0
for index, value in enumerate(numbers[1:], 1):
    if value < numbers[min_index]:
        min_index = index
    if value > numbers[max_index]:
        max_index = index

print(f'{min_index:>2}: {numbers[min_index]}\n{max_index:>2}: {numbers[max_index]}')

numbers[min_index], numbers[max_index] = numbers[max_index], numbers[min_index]
print(numbers)
