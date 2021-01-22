"""
6. По длинам трех отрезков, введенных пользователем, определить возможность существования треугольника,
составленного из этих отрезков. Если такой треугольник существует, то определить, является ли он разносторонним,
равнобедренным или равносторонним.
"""

print('Enter three line lengths:')
len1 = abs(int(input('len1 = ')))
len2 = abs(int(input('len2 = ')))
len3 = abs(int(input('len3 = ')))

if len1 == len2 == len3 and len1 != 0:
    print('Equilateral triangle')
elif (len1 == len2 and len3 < len1 + len2) \
      or (len2 == len3 and len1 < len2 + len3) \
      or (len1 == len3 and len2 < len1 + len3):
    print('Isosceles triangle')
elif (len1 != len2 and len3 < len1 + len2) \
      and (len2 != len3 and len1 < len2 + len3) \
      and (len1 != len3 and len2 < len1 + len3):
    print('Versatile triangle')
else:
    print('Triangle is impossible')
