"""
6. В одномерном массиве найти сумму элементов, находящихся между минимальным и
максимальным элементами. Сами минимальный и максимальный элементы в сумму не включать.
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

left, right = (min_index, max_index) if min_index <= max_index else (max_index, min_index)
element_sum = 0

for value in numbers[left + 1: right]:
    element_sum += value

print(f'Sum = {element_sum}')
