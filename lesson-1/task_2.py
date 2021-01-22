"""
2. По введенным пользователем координатам двух точек вывести уравнение прямой вида y = kx + b, проходящей через эти точки.
"""

print('Input coordinate of point A:')
x1 = int(input('x1: '))
y1 = int(input('y1: '))

print('Input coordinate of point B:')
x2 = int(input('x2: '))
y2 = int(input('y2: '))

if x1 == x2:
    print('It is impossible')
else:
    k = (y2 - y1) / (x2 - x1)
    b = y1 - x1 * (y2 - y1) / (x2 - x1)
    print(f'y = {k} * x {"+" if b >= 0.0 else "-"} {abs(b)}')
