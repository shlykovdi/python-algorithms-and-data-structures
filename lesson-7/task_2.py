"""
2. Отсортируйте по возрастанию методом слияния одномерный вещественный массив, заданный случайными
числами на промежутке [0; 50). Выведите на экран исходный и отсортированный массивы.
"""

import random


def merge_sort(array: []) -> []:
    count = len(array)
    if count > 2:
        part_1 = merge_sort(array[:count // 2])
        part_2 = merge_sort(array[count // 2:])
        array = part_1 + part_2
        last_index = len(array) - 1

        for i in range(last_index):
            min_value = array[i]
            min_index = i

            for j in range(i + 1, last_index + 1):
                if min_value > array[j]:
                    min_value = array[j]
                    min_index = j

            if min_index != i:
                array[i], array[min_index] = array[min_index], array[i]

    elif len(array) > 1 and array[0] > array[1]:
        array[0], array[1] = array[1], array[0]

    return array


size = 10
# Я не нашел в Python констант для float, что-то типа DBL_MIN (C/C++ style), чтобы написать 50.0 - DBL_MIN.
# Поэтому использовал такой длинный float 49.9999999999999999, чтобы удовлетворить условиям задачи [0; 50).
array = [random.uniform(0.0, 49.9999999999999999) for _ in range(size)]
random.shuffle(array)

print(array)
array = merge_sort(array)
print(array)
