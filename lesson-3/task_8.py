"""
8. Матрица 5x4 заполняется вводом с клавиатуры, кроме последних элементов строк.
Программа должна вычислять сумму введенных элементов каждой строки и записывать
ее в последнюю ячейку строки. В конце следует вывести полученную матрицу.
"""

row_count, column_count = 5, 4
matrix = [[0] * column_count for _ in range(row_count)]

print('Fill matrix:')
for row, items in enumerate(matrix):
    element_sum = 0
    for col, _ in enumerate(items[:column_count - 1]):
        matrix[row][col] = int(input(f'[{row}, {col}] = '))
        element_sum += matrix[row][col]
    matrix[row][column_count - 1] = element_sum

print(*matrix, sep='\n')
