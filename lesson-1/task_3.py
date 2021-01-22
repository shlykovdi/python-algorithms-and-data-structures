"""
3. Написать программу, которая генерирует в указанных пользователем границах:
a. случайное целое число,
b. случайное вещественное число,
c. случайный символ.
Для каждого из трех случаев пользователь задает свои границы диапазона.
Например, если надо получить случайный символ от 'a' до 'f', то вводятся эти символы.
Программа должна вывести на экран любой символ алфавита от 'a' до 'f' включительно.
"""

from random import (randint, uniform)


mode = input('Select input mode (i - integer, f - float, c - char): ')

if mode == 'i':
    print('Input integer range:')
    start = int(input('start = '))
    stop = int(input('stop = '))
    print(f'Result: {randint(start, stop)}')
elif mode == 'f':
    print('Input float range:')
    start = float(input('start = '))
    stop = float(input('stop = '))
    print(f'Result: {uniform(start, stop)}')
elif mode == 'c':
    print('Input char range:')
    start = input('start = ')
    stop = input('stop = ')
    print(f'Result: {chr(randint(ord(start), ord(stop)))}')
else:
    print('Unsupported mode')
