import sys
from memory_profiler import profile


print(sys.version, sys.platform)
# 3.8.5 (tags/v3.8.5:580fbb0, Jul 20 2020, 15:57:54) [MSC v.1924 64 bit (AMD64)] win32


ROW_COUNT, COLUMN_COUNT = 800, 600


@profile(precision=5)
def task_impl_1():
    """
    9. Найти максимальный элемент среди минимальных элементов столбцов матрицы.
    """

    matrix = [[row + column for column in range(COLUMN_COUNT)] for row in range(ROW_COUNT)]

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


task_impl_1()

# Max value = 599
# Filename: task_1_impl_1.py
#
# Line #    Mem usage    Increment  Occurences   Line Contents
# ============================================================
#     12  18.42188 MiB  18.42188 MiB           1   @profile(precision=5)
#     13                                         def task_impl_1():
#     14                                             """
#     15                                             9. Найти максимальный элемент среди минимальных элементов столбцов матрицы.
#     16                                             """
#     17
#     18  36.81641 MiB  18.39453 MiB      482403       matrix = [[row + column for column in range(COLUMN_COUNT)] for row in range(ROW_COUNT)]
#     19
#     20  36.81641 MiB   0.00000 MiB           1       min_columns = matrix[0]
#     21  36.83594 MiB   0.01562 MiB         601       for index, values in enumerate(zip(*matrix)):
#     22  36.83594 MiB   0.00391 MiB      480600           for value in values:
#     23  36.83594 MiB   0.00000 MiB      480000               if value < min_columns[index]:
#     24                                                         min_columns[index] = value
#     25
#     26  36.83594 MiB   0.00000 MiB           1       max_value = min_columns[0]
#     27  36.83594 MiB   0.00000 MiB         600       for value in min_columns[1:]:
#     28  36.83594 MiB   0.00000 MiB         599           if value > max_value:
#     29  36.83594 MiB   0.00000 MiB         599               max_value = value
#     30
#     31  36.83594 MiB   0.00000 MiB           1       print(f'Max value = {max_value}')

# Result-1: 36.83594 MiB - 18.42188 MiB = 19308541,379 bytes (~19,30 Mb)
