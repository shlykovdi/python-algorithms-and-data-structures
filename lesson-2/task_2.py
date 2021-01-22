"""
2. Посчитать четные и нечетные цифры введенного натурального числа.
Например, если введено число 34560, в нем 3 четные цифры (4, 6 и 0) и 2 нечетные (3 и 5).
"""

number = int(input('Enter number: '))

even_counter, odd_counter = 0, 0
while number > 0:
    digit = number % 10
    number //= 10
    even_counter += not (digit % 2)
    odd_counter += digit % 2

print(f'Even count = {even_counter}')
print(f'Odd count = {odd_counter}')
