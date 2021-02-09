import sys
from memory_profiler import profile


print(sys.version, sys.platform)
# 3.8.5 (tags/v3.8.5:580fbb0, Jul 20 2020, 15:57:54) [MSC v.1924 64 bit (AMD64)] win32


ROW_COUNT, COLUMN_COUNT = 800, 600


@profile(precision=5)
def task_impl_2():
    """
    9. Найти максимальный элемент среди минимальных элементов столбцов матрицы.
    """

    matrix = []
    for row in range(ROW_COUNT):
        columns = []
        for column in range(COLUMN_COUNT):
            columns.append(row + column)
        matrix.append(columns)

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


task_impl_2()

# Max value = 599
# Filename: task_1_impl_2.py
#
# Line #    Mem usage    Increment  Occurences   Line Contents
# ============================================================
#     12  18.27344 MiB  18.27344 MiB           1   @profile(precision=5)
#     13                                         def task_impl_2():
#     14                                             """
#     15                                             9. Найти максимальный элемент среди минимальных элементов столбцов матрицы.
#     16                                             """
#     17
#     18  18.27344 MiB   0.00000 MiB           1       matrix = []
#     19  36.78125 MiB   0.00391 MiB         801       for row in range(ROW_COUNT):
#     20  36.78125 MiB   0.00391 MiB         800           columns = []
#     21  36.78125 MiB  13.65625 MiB      480800           for column in range(COLUMN_COUNT):
#     22  36.78125 MiB   4.83203 MiB      480000               columns.append(row + column)
#     23  36.78125 MiB   0.01172 MiB         800           matrix.append(columns)
#     24
#     25  36.78125 MiB   0.00000 MiB           1       min_columns = matrix[0]
#     26  36.79688 MiB   0.01562 MiB         601       for index, values in enumerate(zip(*matrix)):
#     27  36.79688 MiB   0.00000 MiB      480600           for value in values:
#     28  36.79688 MiB   0.00000 MiB      480000               if value < min_columns[index]:
#     29                                                         min_columns[index] = value
#     30
#     31  36.79688 MiB   0.00000 MiB           1       max_value = min_columns[0]
#     32  36.79688 MiB   0.00000 MiB         600       for value in min_columns[1:]:
#     33  36.79688 MiB   0.00000 MiB         599           if value > max_value:
#     34  36.79688 MiB   0.00000 MiB         599               max_value = value
#     35
#     36  36.79688 MiB   0.00000 MiB           1       print(f'Max value = {max_value}')

# Result-2: 36.79688 MiB - 18.27344 MiB = 19423234,621 bytes (~19,42 Mb)
