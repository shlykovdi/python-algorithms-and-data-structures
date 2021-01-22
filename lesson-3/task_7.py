"""
7. В одномерном массиве целых чисел определить два наименьших элемента.
Они могут быть как равны между собой (оба минимальны), так и различаться.
"""

from random import randint


numbers = [randint(0, 100) for _ in range(16)]
print(numbers)

min_index_1, min_index_2 = 0, 0
for index, value in enumerate(numbers):
    if value < numbers[min_index_1]:
        min_index_1, min_index_2 = index, min_index_1
    elif value < numbers[min_index_2]:
        min_index_2 = index

print(f'{min_index_1}: {numbers[min_index_1]}\n{min_index_2}: {numbers[min_index_2]}')
