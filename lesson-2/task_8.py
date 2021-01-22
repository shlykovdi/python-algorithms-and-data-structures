"""
8. Посчитать, сколько раз встречается определенная цифра в введенной последовательности чисел.
Количество вводимых чисел и цифра, которую необходимо посчитать, задаются вводом с клавиатуры.
"""

print('Enter number and digit: ')
number = int(input('number = '))
digit = int(input('digit = '))

digit_counter = int(number == 0 == digit)
while number > 0:
    digit_counter += (number % 10 == digit)
    number //= 10

print(f'Digit count = {digit_counter}')
