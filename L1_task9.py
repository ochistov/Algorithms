# -*- coding: utf-8 -*-
"""
Вводятся три разных числа. 
Найти, какое из них является средним (больше одного, но меньше другого).
"""
x1, x2, x3 = [x for x in input('Insert 3 integer numbers divided by space: ').split()]

if x2 < x1 < x3 or x3 < x1 < x2:
    print(f'{x1} is average')
elif x1 < x2 < x3 or x3 < x2 < x1:
    print(f'{x2} is average')
else:
    print(f'{x3} is average')
