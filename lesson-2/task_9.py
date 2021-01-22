"""
9. Среди натуральных чисел, которые были введены, найти наибольшее по сумме цифр.
Вывести на экран это число и сумму его цифр.
"""


def calc_digit_sum(number: int) -> int:
    sum = 0
    while number > 0:
        sum += number % 10
        number //= 10
    return sum


print('Enter numbers separated by comma: ', end='')
number_list = [int(number) for number in input().split(',')]

max = 0
max_sum = 0
for number in number_list:
    sum = calc_digit_sum(number)
    if sum > max_sum:
        max = number
        max_sum = sum

print(f'{max} - {max_sum}')
