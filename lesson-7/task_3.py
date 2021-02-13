"""
3. Массив размером 2m + 1, где m — натуральное число, заполнен случайным образом. Найдите в
массиве медиану. Медианой называется элемент ряда, делящий его на две равные части: в одной
находятся элементы, которые не меньше медианы, в другой — не больше медианы.

Примечание: задачу можно решить без сортировки исходного массива. Но если это слишком сложно,
используйте метод сортировки, который не рассматривался на уроках (сортировка слиянием также недопустима).
"""

import random
from collections import Counter


m = 10
size = 2 * m + 1
array = [random.randint(0, size) for _ in range(size)]
print(array)


counter = Counter()
for i, pivot in enumerate(array):
    for j, value in enumerate(array):
        if i != j:
            if value > pivot:
                counter[pivot] += 1
            elif value < pivot:
                counter[pivot] -= 1

median = None
for value, count in reversed(counter.most_common()):
    if count >= 0:
        median = value
        break

print(counter.most_common())
print(median)
