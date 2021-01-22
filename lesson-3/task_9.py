"""
9. Найти максимальный элемент среди минимальных элементов столбцов матрицы.
"""

from random import randint


row_count, column_count = 5, 4
matrix = [[randint(0, 100) for _ in range(column_count)] for _ in range(row_count)]
print(*matrix, sep='\n', end='\n\n')

min_columns = matrix[0]
for index, values in enumerate(zip(*matrix)):
    for value in values:
        if value < min_columns[index]:
            min_columns[index] = value

max_value = min_columns[0]
for value in min_columns[1:]:
    if value > max_value:
        max_value = value

print(f'Max value = {max_value}')
