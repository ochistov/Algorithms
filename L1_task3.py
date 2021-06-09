# -*- coding: utf-8 -*-
'''По введенным пользователем координатам двух точек вывести уравнение прямой 
вида y=kx+b, проходящей через эти точки.'''

x1, y1 = [int(x) for x in input('Insert coords of first point divided by comma: ').split(',')]
x2, y2 = [int(x) for x in input('Insert coords of second point divided by comma: ').split(',')]
k = (y2 - y1)/(x2 - x1)
b = y1 - k * x1

print(f'Equation of a straight line : y = {k}x + {b}')
