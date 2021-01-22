"""
7. Написать программу, доказывающую или проверяющую, что для множества натуральных
чисел выполняется равенство: 1+2+...+n = n(n+1)/2, где n — любое натуральное число.
"""

n = int(input('Enter N: '))

sum = 0.0
for counter in range(n + 1):
    sum += counter

if sum == n * (n + 1) / 2.0:
    print(f'Confirmed: {sum} == {n * (n + 1) / 2.0}')
else:
    print(f'Busted: {sum} == {n * (n + 1) / 2.0}')
