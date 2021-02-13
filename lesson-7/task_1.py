"""
1. Отсортируйте по убыванию методом пузырька одномерный целочисленный массив,
заданный  случайными числами на промежутке [-100; 100). Выведите на экран исходный и
отсортированный массивы.

Примечания:
a. алгоритм сортировки должен быть в виде функции, которая принимает на вход массив данных,
b. постарайтесь сделать алгоритм умнее, но помните, что у вас должна остаться сортировка пузырьком.
Улучшенные версии сортировки, например, расчёской, шейкерная и другие в зачёт не идут.
"""

import random


def bubble_sort(array: []) -> None:
    for n in range(1, len(array)):
        is_sorted = True
        for i in range(len(array) - n):
            if array[i] < array[i + 1]:
                array[i], array[i + 1] = array[i + 1], array[i]
                is_sorted = False

        if is_sorted:
            break


size = 10
array = [random.randint(-100, 99) for _ in range(size)]
random.shuffle(array)

print(array)
bubble_sort(array)
print(array)
