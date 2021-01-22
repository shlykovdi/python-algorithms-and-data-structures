"""
3. Сформировать из введенного числа обратное по порядку входящих в него цифр и вывести на экран.
Например, если введено число 3486, надо вывести 6843.
"""

number = int(input('Enter number: '))

reverse_number = 0
while number > 0:
    reverse_number *= 10
    reverse_number += number % 10
    number //= 10

print(f'Reverse number = {reverse_number}')
