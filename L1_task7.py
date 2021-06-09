# -*- coding: utf-8 -*-
"""
По длинам трех отрезков, введенных пользователем, определить возможность 
существования треугольника, составленного из этих отрезков. 
Если такой треугольник существует, то определить, является ли он 
разносторонним, равнобедренным или равносторонним.
"""
a, b, c = [float(x) for x in input('Insert the lengths of the line segments divided by space: ').split()]

if a < b + c and b < a + c and c < a + b:
    if a == b and b == c:
        print(f'Triangle with sides {a}, {b}, {c} is equilateral')
    elif a == b or b == c or c == a:
        print(f'Triangle with sides {a}, {b}, {c} is isosceles ')
    else:
        print(f'Triangle with sides {a}, {b}, {c} is scalene')
else:
    print(f'Triangle with sides {a}, {b}, {c} is not exist')
