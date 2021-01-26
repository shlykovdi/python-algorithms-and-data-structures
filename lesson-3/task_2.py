"""
2. Во втором массиве сохранить индексы четных элементов первого массива.
Например, если дан массив со значениями 8, 3, 15, 6, 4, 2, второй массив надо заполнить
значениями 0, 3, 4, 5 (помните, что индексация начинается с нуля), т. к. именно в этих
позициях первого массива стоят четные числа.
"""

from random import randint

numbers = [randint(0, 100) for _ in range(16)]
print(numbers)

even_indexes = [index for index, value in enumerate(numbers) if not value % 2]
print(even_indexes)
