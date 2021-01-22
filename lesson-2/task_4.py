"""
4. Найти сумму n элементов следующего ряда чисел: 1, -0.5, 0.25, -0.125,… Количество элементов (n) вводится с клавиатуры.
"""

n = int(input('Enter element count: '))

element_sum = 0.0
element = 1.0
while n > 0:
    element_sum += element
    element *= -0.5
    n -= 1

print(f'Sum = {element_sum}')
