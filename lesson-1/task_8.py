"""
8. Вводятся три разных числа. Найти, какое из них является средним (больше одного, но меньше другого).
"""

print('Enter three numbers:')
a = int(input('a = '))
b = int(input('b = '))
c = int(input('c = '))

if b <= a <= c or c <= a <= b:
    print(a)
elif a <= b <= c or c <= b <= a:
    print(b)
else:
    print(c)
