import sys
from memory_profiler import profile


print(sys.version, sys.platform)
# 3.8.5 (tags/v3.8.5:580fbb0, Jul 20 2020, 15:57:54) [MSC v.1924 64 bit (AMD64)] win32


ROW_COUNT, COLUMN_COUNT = 800, 600


@profile(precision=5)
def task_impl_3():
    """
    9. Найти максимальный элемент среди минимальных элементов столбцов матрицы.
    """

    matrix = [[row + column for column in range(COLUMN_COUNT)] for row in range(ROW_COUNT)]

    min_columns = matrix[0]
    for column in range(COLUMN_COUNT):
        for row in range(ROW_COUNT):
            if matrix[row][column] < min_columns[column]:
                min_columns[column] = matrix[row][column]

    print(f'Max value = {max(min_columns)}')


task_impl_3()

# 3.8.5 (tags/v3.8.5:580fbb0, Jul 20 2020, 15:57:54) [MSC v.1924 64 bit (AMD64)] win32
# Max value = 599
# Filename: task_1_impl_3.py
#
# Line #    Mem usage    Increment  Occurences   Line Contents
# ============================================================
#     12  18.33594 MiB  18.33594 MiB           1   @profile(precision=5)
#     13                                         def task_impl_3():
#     14                                             """
#     15                                             9. Найти максимальный элемент среди минимальных элементов столбцов матрицы.
#     16                                             """
#     17
#     18  36.73828 MiB  18.40234 MiB      482403       matrix = [[row + column for column in range(COLUMN_COUNT)] for row in range(ROW_COUNT)]
#     19
#     20  36.73828 MiB   0.00000 MiB           1       min_columns = matrix[0]
#     21  36.73828 MiB   0.00000 MiB         601       for column in range(COLUMN_COUNT):
#     22  36.73828 MiB   0.00000 MiB      480600           for row in range(ROW_COUNT):
#     23  36.73828 MiB   0.00000 MiB      480000               if matrix[row][column] < min_columns[column]:
#     24                                                         min_columns[column] = matrix[row][column]
#     25
#     26  36.73828 MiB   0.00000 MiB           1       print(f'Max value = {max(min_columns)}')

# Result-3: 36.73828 MiB - 18.33594 MiB = 19296252,068 bytes (~19,29 Mb)
